import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Video Preview", page_icon="🎬", layout="wide")

st.title("🎬 Preview of Two Local Videos")
st.caption("Videos are loaded from the `videos/` folder in the repository.")

# Paths to video files
VIDEO_DIR = Path(__file__).parent / "videos"
VIDEO_1 = VIDEO_DIR / "video1.mp4"
VIDEO_2 = VIDEO_DIR / "video2.mp4"

# Helper function to load binary content
@st.cache_data(show_spinner=False)
def load_video_bytes(path: Path) -> bytes:
    with path.open("rb") as f:
        return f.read()

# Validate presence of video files
missing = [p.name for p in [VIDEO_1, VIDEO_2] if not p.exists()]
if missing:
    st.error(
        "The following files are missing in the `videos/` folder: "
        + ", ".join(missing)
        + ". Please make sure they are added to the repository."
    )
    st.stop()

# Playback settings in sidebar
with st.sidebar:
    st.header("Settings")
    start_time = st.number_input("Start time (seconds)", min_value=0, value=0, step=1)
    autoplay = st.checkbox("Autoplay", value=False)
    loop = st.checkbox("Loop", value=False)
    muted = st.checkbox("Muted", value=False)
    st.markdown("—")
    st.markdown("**Files:**")
    st.code(str(VIDEO_1), language="bash")
    st.code(str(VIDEO_2), language="bash")

# Layout: two columns side by side
col1, col2 = st.columns(2, gap="large")

with col1:
    st.subheader("Video 1")
    v1_bytes = load_video_bytes(VIDEO_1)
    st.video(v1_bytes, start_time=start_time, autoplay=autoplay, loop=loop, muted=muted)

with col2:
    st.subheader("Video 2")
    v2_bytes = load_video_bytes(VIDEO_2)
    st.video(v2_bytes, start_time=start_time, autoplay=autoplay, loop=loop, muted=muted)

st.success("Videos loaded successfully ✅")
