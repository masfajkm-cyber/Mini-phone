import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="M.Puzzle",
    page_icon="🧩",
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
   PHONE BODY
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

/* =========================
   SCREEN
   ========================= */

.screen {
    width: 100%;
    height: 100%;

    background: #0d1014;
    border-radius: 34px;

    position: relative;
    overflow: hidden;

    border: 1px solid #2c3138;
}

/* =========================
   TOP PHONE DETAILS
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

/* =========================
   LOCK SCREEN
   ========================= */

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

/* =========================
   CLOCK
   ========================= */

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

/* =========================
   BRANDING
   ========================= */

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

/* =========================
   FINGERPRINT
   ========================= */

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

/* =========================
   SCANNING
   ========================= */

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

.instruction {
    margin-top: 18px;

    color: #707884;

    font-size: 11px;
}

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

/* =========================
   GAME HUB
   ========================= */

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
   
