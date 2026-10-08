import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="M.Puzzle",
    page_icon="🧩",
    layout="centered",
    initial_sidebar_state="collapsed"
)

html_code = """
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

/* PHONE */

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

/* SCREEN */

.screen {
    width: 100%;
    height: 100%;

    background: #0d1014;
    border-radius: 34px;

    position: relative;
    overflow: hidden;

    border: 1px solid #2c3138;
}

/* PHONE TOP */

.speaker {
    position: absolute;

    top: 10px;
    left: 50%;

    transform: translateX(-50%);

    width: 58px;
    height: 5px;

    border-radius: 10px;

    background: #252a31;

    z-index: 20;
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

    z-index: 20;
}

/* LOCK SCREEN */

.lock-screen {
    position: absolute;
    inset: 0;

    display: flex;
    flex-direction: column;
    align-items: center;

    padding-top: 68px;

    transition:
        opacity 0.45s ease,
        transform 0.55s ease;
}

.lock-screen.unlocking {
    opacity: 0;
    transform: translateY(-25px);
    pointer-events: none;
}

/* CLOCK */

.time {
    color: #f1f3f5;

    font-size: 54px;
    font-weight: 300;

    letter-spacing: -2px;
}

.date {
    margin-top: 5px;

    color: #858c97;

    font-size: 13px;
}

/* BRAND */

.brand {
    margin-top: 70px;

    color: #f1f3f5;

    font-size: 26px;
    font-weight: 700;

    letter-spacing: -0.8px;
}

.brand-subtitle {
    margin-top: 7px;

    color: #737b86;

    font-size: 10px;

    letter-spacing: 1.8px;

    text-transform: uppercase;
}

.creator {
    margin-top: 8px;

    color: #59616d;

    font-size: 9px;

    letter-spacing: 2px;

    text-transform: uppercase;
}

/* FINGERPRINT */

.fingerprint-area {
    position: absolute;

    bottom: 76px;

    display: flex;
    flex-direction: column;
    align-items: center;
}

.fingerprint {
    width: 82px;
    height: 82px;

    border-radius: 50%;

    border: 1px solid #363d47;

    background: #171b21;

    display: flex;
    align-items: center;
    justify-content: center;

    position: relative;

    cursor: pointer;

    box-shadow:
        0 10px 30px rgba(0,0,0,0.3),
        inset 0 1px 1px rgba(255,255,255,0.04);

    transition:
        transform 0.15s ease,
        border-color 0.15s ease;
}

.fingerprint:active {
    transform: scale(0.96);
}

/* FINGERPRINT ICON */

.fp-icon {
    width: 38px;
    height: 38px;

    border: 3px solid #69727e;

    border-bottom-color: transparent;

    border-radius: 50%;

    position: relative;
}

.fp-icon::before {
    content: "";

    position: absolute;

    width: 22px;
    height: 28px;

    left: 5px;
    top: 7px;

    border: 3px solid #69727e;

    border-bottom-color: transparent;

    border-radius: 50%;
}

.fp-icon::after {
    content: "";

    position: absolute;

    width: 8px;
    height: 18px;

    left: 12px;
    top: 12px;

    border-left: 3px solid #69727e;

    border-radius: 50%;
}

/* SCAN */

.scan-ring {
    position: absolute;

    inset: -7px;

    border-radius: 50%;

    border: 3px solid transparent;

    border-top-color: #5f8cff;

    transform: rotate(-45deg);

    opacity: 0;
}

.fingerprint.scanning {
    border-color: #5f8cff;
}

.fingerprint.scanning .scan-ring {
    opacity: 1;

    animation: scan 1.1s linear infinite;
}

@keyframes scan {

    from {
        transform: rotate(-45deg);
    }

    to {
        transform: rotate(315deg);
    }

}

/* TEXT */

.instruction {
    margin-top: 18px;

    color: #707884;

    font-size: 11px;
}

/* PROGRESS */

.progress {
    margin-top: 9px;

    width: 82px;
    height: 3px;

    background: #242a32;

    border-radius: 10px;

    overflow: hidden;

    opacity: 0;
}

.progress-fill {
    height: 100%;

    width: 0%;

    background: #5f8cff;

    border-radius: inherit;
}

/* GAME HUB */

.game-hub {
    position: absolute;

    inset: 0;

    opacity: 0;

    transform: scale(0.96);

    pointer-events: none;

    transition:
        opacity 0.45s ease,
        transform 0.45s ease;

    padding: 65px 22px 25px;
}

.game-hub.open {
    opacity: 1;

    transform: scale(1);

    pointer-events: auto;
}

.hub-title {
    color: #f1f3f5;

    font-size: 25px;

    font-weight: 700;
}

.hub-subtitle {
    margin-top: 6px;

    color: #737b86;

    font-size: 10px;

    letter-spacing: 1.5px;
}

.hub-creator {
    margin-top: 5px;

    color: #59616d;

    font-size: 9px;

    letter-spacing: 1.5px;

    text-transform: uppercase;
}

/* GAME HUB CARD */

.coming-soon {
    margin-top: 70px;

    padding: 27px 20px;

    border-radius: 22px;

    background: #171b21;

    border: 1px solid #2a3038;

    text-align: center;

    box-shadow:
        0 12px 25px rgba(0,0,0,0.15);
}

.coming-soon-icon {
    font-size: 34px;
}

.coming-soon-title {
    margin-top: 14px;

    color: #e9edf1;

    font-size: 16px;

    font-weight: 600;
}

.coming-soon-text {
    margin-top: 7px;

    color: #727a86;

    font-size: 11px;

    line-height: 1.5;
}

.creator-card {
    margin-top: 22px;

    color: #555d68;

    font-size: 9px;

    letter-spacing: 1.5px;

    text-transform: uppercase;
}

/* HOME BAR */

.home-indicator {
    position: absolute;

    bottom: 8px;

    left: 50%;

    transform: translateX(-50%);

    width: 90px;

    height: 4px;

    border-radius: 10px;

    background: #59616c;

    z-index: 30;
}

/* MOBILE */

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


        <!-- LOCK SCREEN -->

        <div class="lock-screen" id="lockScreen">

            <div class="time" id="time">
                12:00
            </div>

            <div class="date" id="date">
                Loading...
            </div>

            <div class="brand">
                M.Puzzle
            </div>

            <div class="brand-subtitle">
                Mini Game Hub
            </div>

            <div class="creator">
                Made by Masfa
            </div>


            <div class="fingerprint-area">

                <div
                    class="fingerprint"
                    id="fingerprint"
                >

                    <div class="fp-icon"></div>

                    <div class="scan-ring"></div>

                </div>

                <div class="instruction">
                    Press &amp; hold to unlock
                </div>

                <div
                    class="progress"
                    id="progress"
                >

                    <div
                        class="progress-fill"
                        id="progressFill"
                    ></div>

                </div>

            </div>

        </div>


        <!-- GAME HUB -->

        <div
            class="game-hub"
            id="gameHub"
        >

            <div class="hub-title">
                M.Puzzle
            </div>

            <div class="hub-subtitle">
                CHOOSE A GAME
            </div>

            <div class="hub-creator">
                BY MASFA
            </div>

            <div class="coming-soon">

                <div class="coming-soon-icon">
                    🧩
                </div>

                <div class="coming-soon-title">
                    Game Hub
                </div>

                <div class="coming-soon-text">
                    Your mini-games will appear here.
                </div>

                <div class="creator-card">
                    M.PUZZLE • MASFA
                </div>

            </div>

        </div>


        <div class="home-indicator"></div>

    </div>

</div>


<script>

/* CLOCK */

function updateClock() {

    const now = new Date();

    let hours = now.getHours();

    let minutes = now.getMinutes();

    minutes = String(minutes).padStart(2, "0");

    let displayHours = hours % 12;

    if (displayHours === 0) {
        displayHours = 12;
    }

    document.getElementById("time").textContent =
        displayHours + ":" + minutes;

    const options = {
        weekday: "long",
        month: "long",
        day: "numeric"
    };

    document.getElementById("date").textContent =
        now.toLocaleDateString(undefined, options);
}

updateClock();

setInterval(updateClock, 30000);


/* FINGERPRINT */

const fingerprint =
    document.getElementById("fingerprint");

const lockScreen =
    document.getElementById("lockScreen");

const gameHub =
    document.getElementById("gameHub");

const progress =
    document.getElementById("progress");

const progressFill =
    document.getElementById("progressFill");

let holdTimer = null;

let progressTimer = null;

let progressValue = 0;

const HOLD_TIME = 1100;


/* START */

function startScan(event) {

    event.preventDefault();

    if (holdTimer) {
        return;
    }

    fingerprint.classList.add("scanning");

    progress.style.opacity = "1";

    progressValue = 0;

    progressTimer = setInterval(function() {

        progressValue += 100 / (HOLD_TIME / 50);

        if (progressValue >= 100) {
            progressValue = 100;
        }

        progressFill.style.width =
            progressValue + "%";

    }, 50);

    holdTimer = setTimeout(function() {

        unlock();

    }, HOLD_TIME);
}


/* CANCEL */

function cancelScan() {

    if (!holdTimer) {
        return;
    }

    clearTimeout(holdTimer);

    clearInterval(progressTimer);

    holdTimer = null;

    progressTimer = null;

    fingerprint.classList.remove("scanning");

    progressFill.style.width = "0%";

    progress.style.opacity = "0";
}


/* UNLOCK */

function unlock() {

    clearTimeout(holdTimer);

    clearInterval(progressTimer);

    holdTimer = null;

    progressTimer = null;

    progressFill.style.width = "100%";

    setTimeout(function() {

        lockScreen.classList.add("unlocking");

        setTimeout(function() {

            gameHub.classList.add("open");

        }, 220);

    }, 120);
}


/* TOUCH */

fingerprint.addEventListener(
    "touchstart",
    startScan,
    { passive: false }
);

fingerprint.addEventListener(
    "touchend",
    cancelScan
);

fingerprint.addEventListener(
    "touchcancel",
    cancelScan
);


/* MOUSE */

fingerprint.addEventListener(
    "mousedown",
    startScan
);

fingerprint.addEventListener(
    "mouseup",
    cancelScan
);

fingerprint.addEventListener(
    "mouseleave",
    cancelScan
);

</script>

</body>
</html>
"""

components.html(
    html_code,
    height=760,
    scrolling=False
)
   
