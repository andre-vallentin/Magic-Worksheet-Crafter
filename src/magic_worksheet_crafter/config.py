import sys
import tomllib
import shutil
import logging
from dataclasses import dataclass
from pathlib import Path

from docx.shared import RGBColor

logger = logging.getLogger(__name__)

_ASSETS_DIR = Path(__file__).parent / "assets"
_BUNDLED_ICONS = _ASSETS_DIR / "default" / "icons"
_BUNDLED_LOGOS = _ASSETS_DIR / "default" / "logos"
_USER_ASSETS_DIR = _ASSETS_DIR / "user"
_USER_ICONS = _USER_ASSETS_DIR / "icons"
_USER_LOGOS = _USER_ASSETS_DIR / "logos"


def get_config_dir() -> Path:
    if getattr(sys, "frozen", False):
        config_dir = Path.home() / "Library" / "Application Support" / "WorksheetCrafter"
        config_dir.mkdir(parents=True, exist_ok=True)
        return config_dir
    return Path(__file__).parent.parent.parent


def get_config_path() -> Path:
    config_dir = get_config_dir()
    config_path = config_dir / "setup.toml"
    if not config_path.exists():
        _write_default_config(config_path)
    return config_path


def get_user_assets_icons_dir() -> Path:
    """Directory where user-provided replacement icons are stored."""
    if getattr(sys, "frozen", False):
        assets_dir = get_config_dir() / "assets" / "icons"
        assets_dir.mkdir(parents=True, exist_ok=True)
        return assets_dir
    return _USER_ICONS


def get_user_assets_logos_dir() -> Path:
    """Directory where user-provided replacement logos are stored."""
    if getattr(sys, "frozen", False):
        assets_dir = get_config_dir() / "assets" / "logos"
        assets_dir.mkdir(parents=True, exist_ok=True)
        return assets_dir
    return _USER_LOGOS


def _initialize_default_assets() -> None:
    """Copy bundled default assets to user folder if they don't exist (frozen mode only)."""
    if not getattr(sys, "frozen", False):
        return

    user_icons_dir = get_user_assets_icons_dir()
    user_logos_dir = get_user_assets_logos_dir()

    # Copy default icons if they don't exist
    for icon_file in _BUNDLED_ICONS.glob("*.png"):
        user_icon = user_icons_dir / icon_file.name
        if not user_icon.exists():
            shutil.copy2(icon_file, user_icon)
            logger.debug(f"Initialized default icon: {user_icon}")

    # Copy default logo if it doesn't exist
    for logo_file in _BUNDLED_LOGOS.glob("*.png"):
        user_logo = user_logos_dir / logo_file.name
        if not user_logo.exists():
            shutil.copy2(logo_file, user_logo)
            logger.debug(f"Initialized default logo: {user_logo}")


def _normalize_asset_path(path: str) -> str:
    """Convert old absolute paths to new filename-only format."""
    p = Path(path)
    # If it's an old absolute path that doesn't exist, extract just the filename
    if p.is_absolute() and not p.exists():
        logger.debug(f"Migrating old path to filename format: {path} -> {p.name}")
        return p.name
    # If it's already a filename or a valid path, return as-is
    return path


def _resolve_asset(value: str, is_icon: bool = True) -> str:
    """Resolve asset path: check user assets first, then bundled defaults."""
    p = Path(value)

    # Absolute path: use as-is (for backward compatibility)
    if p.is_absolute():
        logger.debug(f"Resolving absolute path: {p}")
        return str(p)

    # Check user assets directory first
    user_assets = get_user_assets_icons_dir() if is_icon else get_user_assets_logos_dir()
    user_asset_path = user_assets / value
    if user_asset_path.exists():
        logger.debug(f"Found user asset: {user_asset_path}")
        return str(user_asset_path)

    # Fall back to bundled assets
    bundled_dir = _BUNDLED_ICONS if is_icon else _BUNDLED_LOGOS
    bundled_path = bundled_dir / value
    logger.debug(f"Using bundled asset: {bundled_path}")
    return str(bundled_path)


@dataclass
class WorksheetConfig:
    color_primary: RGBColor
    color_secondary: RGBColor
    color_primary_hex: str
    color_secondary_hex: str
    logo_path: str
    icon_paths: dict


def _hex_to_rgb(hex_str: str) -> RGBColor:
    h = hex_str.lstrip("#")
    return RGBColor(int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))


def load_config() -> WorksheetConfig:
    _initialize_default_assets()
    config_path = get_config_path()
    logger.debug(f"Loading config from: {config_path}")
    with open(config_path, "rb") as f:
        data = tomllib.load(f)
    primary_hex = data["colors"]["primary"]
    secondary_hex = data["colors"]["secondary"]
    logo_key = "path" if "path" in data["logo"] else "filename"

    # Normalize old absolute paths to new filename format
    logo_value = data["logo"][logo_key]
    logo_value = _normalize_asset_path(logo_value)

    icon_values = {
        "exercise": _normalize_asset_path(data["icons"]["exercise"]),
        "table": _normalize_asset_path(data["icons"]["table"]),
        "single_choice": _normalize_asset_path(data["icons"]["single_choice"]),
        "information": _normalize_asset_path(data["icons"]["information"]),
    }

    config = WorksheetConfig(
        color_primary=_hex_to_rgb(primary_hex),
        color_secondary=_hex_to_rgb(secondary_hex),
        color_primary_hex=primary_hex,
        color_secondary_hex=secondary_hex,
        logo_path=_resolve_asset(logo_value, is_icon=False),
        icon_paths={
            "exercise":      _resolve_asset(icon_values["exercise"], is_icon=True),
            "table":         _resolve_asset(icon_values["table"], is_icon=True),
            "single_choice": _resolve_asset(icon_values["single_choice"], is_icon=True),
            "information":   _resolve_asset(icon_values["information"], is_icon=True),
        },
    )
    logger.debug(f"Loaded icon paths: {config.icon_paths}")
    return config


def save_config(
    primary_hex: str,
    secondary_hex: str,
    logo_path: str,
    icon_paths: dict,
) -> None:
    config_path = get_config_path()
    user_icons_dir = get_user_assets_icons_dir()
    user_logos_dir = get_user_assets_logos_dir()

    # Process logo: copy to user assets if it's a new user-provided file
    logo_filename = "logo.png"
    logo_src = Path(logo_path)
    logo_dest = user_logos_dir / logo_filename
    if logo_src.exists() and logo_src != logo_dest:
        shutil.copy2(logo_src, logo_dest)

    # Process icon paths: copy to user assets if they're new user-provided files
    icon_filenames = {}
    icon_map = {
        "exercise": "exercise.png",
        "table": "table.png",
        "single_choice": "single_choice.png",
        "information": "information.png",
    }

    for icon_key, icon_name in icon_map.items():
        src_path = Path(icon_paths[icon_key])
        dest_path = user_icons_dir / icon_name

        if src_path.exists():
            # If it's a user-provided file (not already in user assets), copy it
            if src_path != dest_path:
                shutil.copy2(src_path, dest_path)
            icon_filenames[icon_key] = icon_name
        else:
            # File doesn't exist, use the filename only
            icon_filenames[icon_key] = src_path.name

    content = f"""[colors]
primary   = "{primary_hex}"
secondary = "{secondary_hex}"

[logo]
path = "{logo_filename}"

[icons]
exercise      = "{icon_filenames['exercise']}"
table         = "{icon_filenames['table']}"
single_choice = "{icon_filenames['single_choice']}"
information   = "{icon_filenames['information']}"
"""
    config_path.write_text(content, encoding="utf-8")


def _write_default_config(path: Path) -> None:
    content = """[colors]
primary   = "#FF6F4A"
secondary = "#01A976"

[logo]
path = "logo.png"

[icons]
exercise      = "exercise.png"
table         = "table.png"
single_choice = "tick_task.png"
information   = "info_text.png"
"""
    path.write_text(content, encoding="utf-8")
