import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="M.Puzzle",
    page_icon="📱",
    layout="centered",
    initial_sidebar_state="collapsed"
)

components.html("""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
* {
    box-sizing: border-box;
    -webkit-tap-highlight-color: transparent;
}

html, body {
    margin: 0;
    padding: 0;
    width: 100%;
    min-height: 100%;
    background: transparent;
    font-family: Arial, Helvetica, sans-serif;
}

body {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px 0;
}

/* =========================
   MINI PHONE
   ========================= */

.phone {
    width: min(360px, 92vw);
    height: min(720px, 88vh);
    min-height: 600px;

    background: #20242a;
    border: 2px solid #353a42;
    border-radius: 42px;

    padding: 10px;

    box-shadow:
        0 25px 60px rgba(0,0,0,0.28),
        inset 0 1px 1px rgba(255,255,255,0.10);

    position: relative;
}

/* Inner screen */

.screen {
    width: 100%;
    height: 100%;

    background: #101318;
    border-radius: 34px;

    position: relative;
    overflow: hidden;

    border: 1px solid #2c3138;
}

/* =========================
   TOP HARDWARE
   ========================= */

.speaker {
    position: absolute;
    top: 10px;
    left: 50%;
    transform: translateX(-50%);

    width: 58px;
    height: 5px;

    border-radius: 10px;
    background: #252a31;

    z-index: 10;
}

.camera {
    position: absolute;
    top: 8px;
    right: 82px;

    width: 7px;
    height: 7px;

    border-radius: 50%;
    background: #080a0d;

    border: 1px solid #3b414a;

    z-index: 10;
}

/* =========================
   SCREEN CONTENT
   ========================= */

.content {
    height: 100%;

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;

    padding: 40px 25px;
}

.logo {
    font-size: 30px;
    font-weight: 700;
    letter-spacing: -1px;
    color: #f2f4f7;
}

.subtitle {
    margin-top: 8px;

    font-size: 13px;
    letter-spacing: 1.5px;
    text-transform: uppercase;

    color: #858c97;
}

/* Decorative center */

.center-icon {
    margin-top: 55px;

    width: 92px;
    height: 92px;

    border-radius: 28px;

    display: flex;
    justify-content: center;
    align-items: center;

    background: #1a1f26;
    border: 1px solid #303640;

    box-shadow:
        0 12px 30px rgba(0,0,0,0.25),
        inset 0 1px 1px rgba(255,255,255,0.04);

    font-size: 38px;
}

.status {
    margin-top: 25px;

    font-size: 12px;
    color: #777f8b;

    letter-spacing: 0.5px;
}

/* =========================
   BOTTOM NAV PREVIEW
   ========================= */

.bottom-bar {
    position: absolute;

    left: 25px;
    right: 25px;
    bottom: 20px;

    height: 54px;

    border-radius: 20px;

    background: #181c22;
    border: 1px solid #292f37;

    display: flex;
    align-items: center;
    justify-content: center;

    color: #656d78;

    font-size: 11px;
    letter-spacing: 1px;
}

/* =========================
   HOME INDICATOR
   ========================= */

.home-indicator {
    position: absolute;

    bottom: 8px;
    left: 50%;
    transform: translateX(-50%);

    width: 90px;
    height: 4px;

    border-radius: 10px;

    background: #59616c;
}

/* =========================
   RESPONSIVE
   ========================= */

@media (max-height: 700px) {
    .phone {
        height: 600px;
        min-height: 600px;
    }
}

@media (max-width: 380px) {
    .phone {
        width: 94vw;
        border-radius: 38px;
    }

    .screen {
        border-radius: 31px;
    }
}
</style>
</head>

<body>

<div class="phone">

    <div class="screen">

        <div class="speaker"></div>
        <div class="camera"></div>

        <div class="content">

            <div class="logo">M.Puzzle</div>

            <div class="subtitle">
                Mini Game Hub
            </div>

            <div class="center-icon">
                🧩
            </div>

            <div class="status">
                Your games. One place.
            </div>

        </div>

        <div class="bottom-bar">
            M.PUZZLE
        </div>

        <div class="home-indicator"></div>

    </div>

</div>

</body>
</html>
""", height=760, scrolling=False)
