import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="AURA WAR",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

HTML = r"""
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
*{
    box-sizing:border-box;
    user-select:none;
}

html,body{
    margin:0;
    padding:0;
    width:100%;
    min-height:100%;
    background:#050713;
    font-family:Arial,Helvetica,sans-serif;
    color:white;
    overflow-x:hidden;
}

body{
    display:flex;
    justify-content:center;
}

#app{
    width:100%;
    max-width:1550px;
    margin:auto;
    padding:16px;
}

.hidden{
    display:none !important;
}

/* ================= HOME ================= */

#home{
    width:100%;
    min-height:100vh;
    display:flex;
    flex-direction:column;
    align-items:center;
    padding:20px 10px 40px;
}

.logo{
    font-size:58px;
    font-weight:1000;
    letter-spacing:8px;
    text-align:center;
    color:#ffffff;
    text-shadow:
        0 0 8px #6ff5ff,
        0 0 22px #477cff,
        0 0 50px #8c52ff;
    margin-top:5px;
}

.subtitle{
    font-size:18px;
    font-weight:800;
    letter-spacing:5px;
    color:#aebdff;
    margin-bottom:20px;
}

.home-panel{
    width:100%;
    max-width:1450px;
    padding:24px;
    border:1px solid rgba(140,180,255,.35);
    border-radius:28px;
    background:
        radial-gradient(circle at 15% 10%,rgba(60,150,255,.13),transparent 30%),
        radial-gradient(circle at 85% 90%,rgba(180,70,255,.12),transparent 30%),
        rgba(10,15,34,.92);
    box-shadow:
        0 0 50px rgba(60,120,255,.14),
        inset 0 0 50px rgba(255,255,255,.025);
}

.home-title{
    font-size:25px;
    font-weight:1000;
    text-align:center;
    margin-bottom:18px;
}

.name-row{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:16px;
    margin-bottom:20px;
}

.name-box{
    padding:15px;
    border-radius:18px;
    background:rgba(255,255,255,.045);
    border:1px solid rgba(255,255,255,.12);
}

.name-box label{
    display:block;
    font-size:17px;
    font-weight:900;
    margin-bottom:8px;
}

.name-box input{
    width:100%;
    padding:13px 15px;
    border:none;
    outline:none;
    border-radius:12px;
    background:#080d20;
    color:white;
    font-size:18px;
    font-weight:700;
}

.mode-row{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:16px;
    margin-bottom:24px;
}

.mode-btn{
    min-height:75px;
    border:none;
    border-radius:18px;
    cursor:pointer;
    color:white;
    font-size:22px;
    font-weight:1000;
    background:linear-gradient(135deg,#192652,#252c63);
    border:2px solid rgba(255,255,255,.12);
    transition:.2s;
}

.mode-btn:hover{
    transform:translateY(-3px);
    filter:brightness(1.2);
}

.mode-btn.active{
    border-color:#69e8ff;
    box-shadow:
        0 0 20px rgba(80,220,255,.45),
        inset 0 0 25px rgba(80,180,255,.12);
    background:linear-gradient(135deg,#174c7d,#433181);
}

.section-title{
    text-align:center;
    font-size:24px;
    font-weight:1000;
    margin:18px 0 14px;
}

.char-grid{
    display:grid;
    grid-template-columns:repeat(6,1fr);
    gap:12px;
}

.char-card{
    position:relative;
    min-height:190px;
    padding:13px 9px;
    border-radius:18px;
    border:2px solid rgba(255,255,255,.1);
    background:linear-gradient(160deg,#11182f,#090d1c);
    cursor:pointer;
    transition:.18s;
    overflow:hidden;
}

.char-card:hover{
    transform:translateY(-5px);
    border-color:rgba(255,255,255,.45);
}

.char-card.p1-selected{
    border-color:#5ceaff;
    box-shadow:
        0 0 18px rgba(70,230,255,.55),
        inset 0 0 20px rgba(70,230,255,.1);
}

.char-card.p2-selected{
    border-color:#ff73dc;
    box-shadow:
        0 0 18px rgba(255,80,220,.5),
        inset 0 0 20px rgba(255,80,220,.1);
}

.char-icon{
    font-size:48px;
    text-align:center;
    margin:4px 0 4px;
}

.char-name{
    text-align:center;
    font-size:18px;
    font-weight:1000;
}

.char-element{
    text-align:center;
    font-size:13px;
    font-weight:900;
    opacity:.8;
    margin-top:3px;
}

.char-skill{
    text-align:center;
    font-size:12px;
    font-weight:700;
    opacity:.72;
    margin-top:8px;
}

.start-btn{
    display:block;
    margin:25px auto 0;
    padding:16px 45px;
    border:0;
    border-radius:18px;
    cursor:pointer;
    color:white;
    font-size:23px;
    font-weight:1000;
    background:linear-gradient(135deg,#276fff,#8a3cff);
    box-shadow:
        0 0 25px rgba(90,100,255,.35),
        inset 0 1px rgba(255,255,255,.3);
    transition:.2s;
}

.start-btn:hover{
    transform:scale(1.04);
    box-shadow:
        0 0 38px rgba(90,100,255,.55),
        inset 0 1px rgba(255,255,255,.3);
}

/* ================= GAME ================= */

#game{
    width:100%;
    display:flex;
    flex-direction:column;
    align-items:center;
}

#gameHeader{
    width:100%;
    max-width:1500px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:14px;
    margin-bottom:10px;
}

.playerPanel{
    flex:1;
    min-width:0;
}

.playerName{
    font-size:19px;
    font-weight:1000;
    margin-bottom:5px;
    white-space:nowrap;
    overflow:hidden;
    text-overflow:ellipsis;
}

.hpOuter,
.energyOuter{
    width:100%;
    height:18px;
    border-radius:12px;
    overflow:hidden;
    background:#111525;
    border:1px solid rgba(255,255,255,.2);
}

.hpInner{
    height:100%;
    width:100%;
    background:linear-gradient(90deg,#36e77c,#b7ff67);
    transition:width .12s;
}

.p2hp{
    background:linear-gradient(90deg,#ff5477,#ffb15c);
}

.energyOuter{
    height:10px;
    margin-top:4px;
}

.energyInner{
    height:100%;
    width:0%;
    background:linear-gradient(90deg,#36cfff,#a06cff);
    transition:width .12s;
}

#timer{
    min-width:100px;
    text-align:center;
    font-size:39px;
    font-weight:1000;
    text-shadow:0 0 15px #6cecff;
}

#arenaWrap{
    width:100%;
    max-width:1500px;
    position:relative;
    border-radius:25px;
    overflow:hidden;
    border:2px solid rgba(120,190,255,.42);
    background:#050816;
    box-shadow:
        0 0 40px rgba(40,130,255,.18),
        0 0 100px rgba(90,50,255,.08);
}

#canvas{
    display:block;
    width:100%;
    height:auto;
    min-height:690px;
    background:#050816;
}

#countdown{
    position:absolute;
    inset:0;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:110px;
    font-weight:1000;
    color:white;
    text-shadow:
        0 0 20px #66eaff,
        0 0 55px #6f55ff;
    pointer-events:none;
    z-index:20;
}

#result{
    position:absolute;
    inset:0;
    display:flex;
    align-items:center;
    justify-content:center;
    z-index:30;
    background:rgba(3,5,18,.5);
}

.resultBox{
    min-width:400px;
    max-width:80%;
    padding:32px 42px;
    text-align:center;
    border-radius:25px;
    border:2px solid rgba(255,255,255,.25);
    background:rgba(8,12,32,.94);
    box-shadow:0 0 60px rgba(80,160,255,.3);
}

.resultTitle{
    font-size:45px;
    font-weight:1000;
    margin-bottom:12px;
}

.resultText{
    font-size:22px;
    font-weight:800;
    color:#dce5ff;
}

.resultButtons{
    display:flex;
    justify-content:center;
    gap:12px;
    margin-top:25px;
}

.resultButtons button{
    border:0;
    border-radius:13px;
    padding:12px 22px;
    color:white;
    font-size:17px;
    font-weight:900;
    cursor:pointer;
    background:#30457e;
}

.resultButtons button:hover{
    filter:brightness(1.2);
}

/* ================= CHARACTER INFO ================= */

#selectionInfo{
    width:100%;
    max-width:1500px;
    margin-top:15px;
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:15px;
}

.infoBox{
    padding:16px 20px;
    border-radius:18px;
    background:rgba(13,18,39,.9);
    border:1px solid rgba(255,255,255,.12);
}

.infoBox h3{
    margin:0 0 7px;
    font-size:20px;
}

.infoBox p{
    margin:0;
    font-size:16px;
    font-weight:700;
    line-height:1.5;
}

/* ================= CONTROLS ================= */

#instructions{
    width:100%;
    max-width:1500px;
    margin-top:18px;
    padding:24px;
    border-radius:22px;
    background:
        linear-gradient(145deg,rgba(15,22,49,.98),rgba(8,12,27,.98));
    border:1px solid rgba(120,170,255,.22);
}

#instructions h2{
    text-align:center;
    font-size:29px;
    margin:0 0 20px;
}

.controlGrid{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:18px;
}

.controlBox{
    padding:20px;
    border-radius:17px;
    background:rgba(255,255,255,.045);
    border:1px solid rgba(255,255,255,.1);
}

.controlBox h3{
    margin:0 0 12px;
    font-size:21px;
}

.controlBox p{
    margin:7px 0;
    font-size:17px;
    line-height:1.55;
    font-weight:700;
    color:#e6ebff;
}

.key{
    display:inline-block;
    min-width:32px;
    padding:4px 8px;
    margin:2px;
    text-align:center;
    border-radius:7px;
    background:#171e3a;
    border:1px solid #5a6fae;
    color:white;
    font-weight:1000;
}

/* ================= BALLOONS ================= */

.balloon{
    position:fixed;
    bottom:-100px;
    width:25px;
    height:34px;
    border-radius:50% 50% 45% 45%;
    z-index:100;
    animation:balloonUp linear forwards;
    pointer-events:none;
}

.balloon:after{
    content:"";
    position:absolute;
    left:50%;
    top:100%;
    width:1px;
    height:75px;
    background:rgba(255,255,255,.45);
}

@keyframes balloonUp{
    0%{
        transform:translateY(0) rotate(0deg);
        opacity:0;
    }
    10%{
        opacity:1;
    }
    100%{
        transform:translateY(-115vh) rotate(18deg);
        opacity:.9;
    }
}

/* ================= RESPONSIVE ================= */

@media(max-width:1050px){
    .char-grid{
        grid-template-columns:repeat(3,1fr);
    }

    #canvas{
        min-height:550px;
    }
}

@media(max-width:720px){
    #app{
        padding:8px;
    }

    .logo{
        font-size:38px;
        letter-spacing:4px;
    }

    .name-row,
    .mode-row,
    .controlGrid,
    #selectionInfo{
        grid-template-columns:1fr;
    }

    .char-grid{
        grid-template-columns:repeat(2,1fr);
    }

    #timer{
        min-width:65px;
        font-size:27px;
    }

    #countdown{
        font-size:70px;
    }

    #canvas{
        min-height:480px;
    }

    .resultBox{
        min-width:0;
        width:88%;
        padding:25px;
    }
}
</style>
</head>

<body>
<div id="app">

<!-- ================= HOME ================= -->

<div id="home">

    <div class="logo">AURA WAR</div>
    <div class="subtitle">⚡ ANIME 1V1 BATTLE ⚡</div>

    <div class="home-panel">

        <div class="home-title">THIẾT LẬP TRẬN ĐẤU</div>

        <div class="name-row">

            <div class="name-box">
                <label>🔵 Tên người chơi 1</label>
                <input id="p1NameInput"
                       maxlength="20"
                       placeholder="Nhập tên P1...">
            </div>

            <div class="name-box" id="p2NameBox">
                <label>🟣 Tên người chơi 2</label>
                <input id="p2NameInput"
                       maxlength="20"
                       placeholder="Nhập tên P2...">
            </div>

        </div>

        <div class="mode-row">

            <button class="mode-btn active" id="mode1v1">
                ⚔️ 1V1
            </button>

            <button class="mode-btn" id="modeCPU">
                🤖 VS MÁY
            </button>

        </div>

        <div class="section-title">
            CHỌN NHÂN VẬT
        </div>

        <div class="char-grid" id="charGrid">

            <div class="char-card p1-selected"
                 data-char="water">
                <div class="char-icon">🌊</div>
                <div class="char-name">KAIRO</div>
                <div class="char-element">THỦY</div>
                <div class="char-skill">
                    Thủy Long • Hải Long Diệt
                </div>
            </div>

            <div class="char-card"
                 data-char="fire">
                <div class="char-icon">🔥</div>
                <div class="char-name">RENJI</div>
                <div class="char-element">VIÊM</div>
                <div class="char-skill">
                    Hỏa Lưu • Viêm Long Phá
                </div>
            </div>

            <div class="char-card"
                 data-char="thunder">
                <div class="char-icon">⚡</div>
                <div class="char-name">RAI</div>
                <div class="char-element">LÔI</div>
                <div class="char-skill">
                    Lôi Kích • Thiên Lôi
                </div>
            </div>

            <div class="char-card"
                 data-char="flower">
                <div class="char-icon">🌸</div>
                <div class="char-name">MIZUHA</div>
                <div class="char-element">HOA</div>
                <div class="char-skill">
                    Hoa Vũ • Bách Hoa Loạn Vũ
                </div>
            </div>

            <div class="char-card"
                 data-char="rock">
                <div class="char-icon">🪨</div>
                <div class="char-name">GARO</div>
                <div class="char-element">ĐÁ</div>
                <div class="char-skill">
                    Nham Kích • Đại Địa Chấn
                </div>
            </div>

            <div class="char-card"
                 data-char="wind">
                <div class="char-icon">🌪️</div>
                <div class="char-name">KAZE</div>
                <div class="char-element">GIÓ</div>
                <div class="char-skill">
                    Cuồng Phong • Thiên Phong Loạn Vũ
                </div>
            </div>

        </div>

        <button class="start-btn" id="startBtn">
            ▶ BẮT ĐẦU TRẬN
        </button>

    </div>

</div>

<!-- ================= GAME ================= -->

<div id="game" class="hidden">

    <div id="gameHeader">

        <div class="playerPanel">
            <div class="playerName" id="p1NameHud">P1</div>

            <div class="hpOuter">
                <div class="hpInner" id="p1Hp"></div>
            </div>

            <div class="energyOuter">
                <div class="energyInner" id="p1Energy"></div>
            </div>
        </div>

        <div id="timer">60</div>

        <div class="playerPanel">
            <div class="playerName" id="p2NameHud"
                 style="text-align:right">
                P2
            </div>

            <div class="hpOuter">
                <div class="hpInner p2hp"
                     id="p2Hp"
                     style="margin-left:auto">
                </div>
            </div>

            <div class="energyOuter">
                <div class="energyInner"
                     id="p2Energy"
                     style="margin-left:auto">
                </div>
            </div>
        </div>

    </div>

    <div id="arenaWrap">

        <canvas id="canvas"
                width="1500"
                height="820">
        </canvas>

        <div id="countdown">3</div>

        <div id="result" class="hidden">

            <div class="resultBox">

                <div class="resultTitle"
                     id="resultTitle">
                    VICTORY
                </div>

                <div class="resultText"
                     id="resultText">
                </div>

                <div class="resultButtons">

                    <button id="againBtn">
                        🔄 ĐÁNH LẠI
                    </button>

                    <button id="homeBtn">
                        🏠 VỀ MENU
                    </button>

                </div>

            </div>

        </div>

    </div>

    <div id="selectionInfo">

        <div class="infoBox">
            <h3>🔵 P1</h3>
            <p id="p1CharInfo">KAIRO • THỦY</p>
        </div>

        <div class="infoBox">
            <h3>🟣 P2</h3>
            <p id="p2CharInfo">RENJI • VIÊM</p>
        </div>

    </div>

    <!-- HƯỚNG DẪN ĐÃ ĐƯA XUỐNG DƯỚI -->

    <div id="instructions">

        <h2>🎮 HƯỚNG DẪN</h2>

        <div class="controlGrid">

            <div class="controlBox">

                <h3>🔵 NGƯỜI CHƠI 1</h3>

                <p>
                    <span class="key">A</span>
                    <span class="key">D</span>
                    Di chuyển
                </p>

                <p>
                    <span class="key">W</span>
                    Nhảy
                </p>

                <p>
                    <span class="key">S</span>
                    Rơi nhanh
                </p>

                <p>
                    <span class="key">J</span>
                    Đánh thường
                </p>

                <p>
                    <span class="key">K</span>
                    Skill
                </p>

                <p>
                    <span class="key">L</span>
                    Dash
                </p>

                <p>
                    <span class="key">U</span>
                    Heavy
                </p>

                <p>
                    <span class="key">I</span>
                    Ultimate
                </p>

            </div>

            <div class="controlBox">

                <h3>🟣 NGƯỜI CHƠI 2</h3>

                <p>
                    <span class="key">←</span>
                    <span class="key">→</span>
                    Di chuyển
                </p>

                <p>
                    <span class="key">↑</span>
                    Nhảy
                </p>

                <p>
                    <span class="key">↓</span>
                    Rơi nhanh
                </p>

                <p>
                    <span class="key">1</span>
                    Đánh thường
                </p>

                <p>
                    <span class="key">2</span>
                    Skill
                </p>

                <p>
                    <span class="key">3</span>
                    Dash
                </p>

                <p>
                    <span class="key">4</span>
                    Heavy
                </p>

                <p>
                    <span class="key">5</span>
                    Ultimate
                </p>

            </div>

        </div>

    </div>

</div>

</div>

<script>
/* =========================================================
   AURA WAR
   PHYSICS-SAFE VERSION
   ========================================================= */

const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

const W = canvas.width;
const H = canvas.height;

const FLOOR_Y = H - 150;

/* ================= CHARACTERS ================= */

const CHARACTERS = {

    water:{
        name:"KAIRO",
        element:"THỦY",
        color:"#36c8ff",
        dark:"#1268a4",
        light:"#a7edff",
        accent:"#227aff",
        skillName:"THỦY LONG",
        ultimateName:"HẢI LONG DIỆT",
        icon:"🌊",
        style:"water"
    },

    fire:{
        name:"RENJI",
        element:"VIÊM",
        color:"#ff5638",
        dark:"#a92319",
        light:"#ffd09a",
        accent:"#ff9d24",
        skillName:"HỎA LƯU",
        ultimateName:"VIÊM LONG PHÁ",
        icon:"🔥",
        style:"fire"
    },

    thunder:{
        name:"RAI",
        element:"LÔI",
        color:"#ffe84b",
        dark:"#ad8610",
        light:"#fff9bd",
        accent:"#fff06a",
        skillName:"LÔI KÍCH",
        ultimateName:"THIÊN LÔI",
        icon:"⚡",
        style:"thunder"
    },

    flower:{
        name:"MIZUHA",
        element:"HOA",
        color:"#ff7ccf",
        dark:"#a82e78",
        light:"#ffd8f0",
        accent:"#ffb0e3",
        skillName:"HOA VŨ",
        ultimateName:"BÁCH HOA LOẠN VŨ",
        icon:"🌸",
        style:"flower"
    },

    rock:{
        name:"GARO",
        element:"ĐÁ",
        color:"#b8a98e",
        dark:"#635848",
        light:"#e2d7bd",
        accent:"#8e8068",
        skillName:"NHAM KÍCH",
        ultimateName:"ĐẠI ĐỊA CHẤN",
        icon:"🪨",
        style:"rock"
    },

    wind:{
        name:"KAZE",
        element:"GIÓ",
        color:"#6ff5d0",
        dark:"#218c78",
        light:"#d5fff4",
        accent:"#9bffe9",
        skillName:"CUỒNG PHONG",
        ultimateName:"THIÊN PHONG LOẠN VŨ",
        icon:"🌪️",
        style:"wind"
    }
};

const charKeys = Object.keys(CHARACTERS);

let mode = "1v1";
let selectedP1 = "water";
let selectedP2 = "fire";

let gameRunning = false;
let gameStarted = false;
let countdownRunning = false;

let p1 = null;
let p2 = null;

let projectiles = [];
let particles = [];
let effects = [];
let afterimages = [];

let timeLeft = 60;
let lastTime = 0;

let keys = {};

let audioCtx = null;
let masterGain = null;
let soundEnabled = true;

/* ================= AUDIO ================= */

function initAudio(){

    if(!audioCtx){

        audioCtx = new (
            window.AudioContext ||
            window.webkitAudioContext
        )();

        masterGain = audioCtx.createGain();

        masterGain.gain.value = .24;

        masterGain.connect(
            audioCtx.destination
        );
    }

    if(audioCtx.state === "suspended"){
        audioCtx.resume();
    }
}

function tone(
    freq,
    duration,
    type="sine",
    gain=.08,
    endFreq=null
){

    if(!soundEnabled) return;

    initAudio();

    const osc =
        audioCtx.createOscillator();

    const g =
        audioCtx.createGain();

    osc.type = type;

    osc.frequency.setValueAtTime(
        freq,
        audioCtx.currentTime
    );

    if(endFreq !== null){

        osc.frequency.exponentialRampToValueAtTime(
            Math.max(30,endFreq),
            audioCtx.currentTime + duration
        );
    }

    g.gain.setValueAtTime(
        .0001,
        audioCtx.currentTime
    );

    g.gain.exponentialRampToValueAtTime(
        gain,
        audioCtx.currentTime + .015
    );

    g.gain.exponentialRampToValueAtTime(
        .0001,
        audioCtx.currentTime + duration
    );

    osc.connect(g);
    g.connect(masterGain);

    osc.start();

    osc.stop(
        audioCtx.currentTime +
        duration +
        .03
    );
}

function noise(
    duration=.12,
    gain=.08,
    filterFreq=1800
){

    if(!soundEnabled) return;

    initAudio();

    const buffer =
        audioCtx.createBuffer(
            1,
            audioCtx.sampleRate * duration,
            audioCtx.sampleRate
        );

    const data =
        buffer.getChannelData(0);

    for(let i=0;i<data.length;i++){

        data[i] =
            Math.random()*2-1;
    }

    const source =
        audioCtx.createBufferSource();

    const filter =
        audioCtx.createBiquadFilter();

    const g =
        audioCtx.createGain();

    filter.type = "bandpass";
    filter.frequency.value = filterFreq;
    filter.Q.value = .7;

    g.gain.setValueAtTime(
        gain,
        audioCtx.currentTime
    );

    g.gain.exponentialRampToValueAtTime(
        .0001,
        audioCtx.currentTime + duration
    );

    source.buffer = buffer;

    source.connect(filter);
    filter.connect(g);
    g.connect(masterGain);

    source.start();
}

function sfxSlash(){

    tone(480,.08,"sawtooth",.055,950);
    noise(.055,.035,2800);
}

function sfxHeavy(){

    tone(120,.18,"square",.10,55);
    noise(.18,.12,700);
    tone(260,.12,"triangle",.05,80);
}

function sfxHit(){

    noise(.10,.09,950);
    tone(95,.10,"square",.055,45);
}

function sfxDash(style="normal"){

    if(style==="wind"){

        noise(.32,.075,3200);
        tone(500,.28,"sine",.035,1100);

    }else{

        noise(.18,.055,2400);
        tone(240,.16,"sawtooth",.035,800);
    }
}

function sfxSkill(style){

    if(style==="water"){

        tone(330,.35,"sine",.06,720);
        tone(520,.30,"sine",.045,980);
        noise(.16,.025,1800);

    }else if(style==="fire"){

        noise(.30,.09,900);
        tone(180,.25,"sawtooth",.055,70);
        tone(480,.18,"triangle",.04,120);

    }else if(style==="thunder"){

        tone(900,.12,"square",.07,180);
        tone(1450,.08,"square",.055,400);
        noise(.13,.07,4200);

    }else if(style==="flower"){

        tone(520,.35,"sine",.05,900);
        tone(780,.42,"sine",.04,1250);

    }else if(style==="rock"){

        tone(90,.32,"square",.09,45);
        noise(.28,.10,500);

    }else if(style==="wind"){

        noise(.55,.075,3800);
        tone(420,.48,"sine",.045,1200);
        tone(720,.35,"triangle",.025,1450);

    }else{

        tone(400,.25,"sine",.05,800);
    }
}

function sfxUltimate(style){

    tone(180,.30,"sine",.06,420);
    tone(360,.40,"sine",.055,900);

    setTimeout(()=>{

        if(!soundEnabled) return;

        noise(.45,.16,1100);
        tone(75,.45,"square",.12,35);
        tone(600,.32,"sawtooth",.065,100);

        if(style==="wind"){

            noise(.65,.10,4500);
            tone(900,.60,"sine",.05,1600);

        }else if(style==="thunder"){

            tone(1100,.22,"square",.09,120);
            noise(.35,.10,5000);

        }else if(style==="fire"){

            noise(.55,.14,800);
            tone(180,.40,"sawtooth",.08,45);

        }else if(style==="water"){

            tone(300,.55,"sine",.07,950);
            noise(.35,.05,1800);

        }else if(style==="rock"){

            tone(65,.60,"square",.14,30);
            noise(.55,.13,450);

        }else if(style==="flower"){

            tone(600,.55,"sine",.06,1300);
            tone(900,.50,"sine",.04,1600);
        }

    },260);
}

function sfxJump(){
    tone(280,.10,"sine",.035,620);
}

function sfxCountdown(n){

    if(n===1){

        tone(
            880,
            .18,
            "square",
            .07,
            620
        );

    }else{

        tone(
            440,
            .18,
            "square",
            .065,
            320
        );
    }
}

function sfxFight(){

    tone(
        420,
        .16,
        "sawtooth",
        .08,
        900
    );

    tone(
        900,
        .35,
        "sine",
        .07,
        1500
    );

    noise(.12,.04,3000);
}

function sfxVictory(){

    tone(523,.18,"sine",.07,660);

    setTimeout(()=>{
        tone(659,.18,"sine",.07,830);
    },140);

    setTimeout(()=>{
        tone(784,.35,"sine",.09,1100);
    },280);
}

function sfxDefeat(){

    tone(320,.25,"sine",.06,220);

    setTimeout(()=>{
        tone(220,.40,"sine",.065,100);
    },180);
}

/* ================= INPUT ================= */

window.addEventListener(
    "keydown",
    function(e){

        const key =
            e.key.toLowerCase();

        keys[key] = true;

        if([
            "arrowup",
            "arrowdown",
            "arrowleft",
            "arrowright",
            " "
        ].includes(key)){

            e.preventDefault();
        }
    }
);

window.addEventListener(
    "keyup",
    function(e){

        keys[
            e.key.toLowerCase()
        ] = false;
    }
);

/* ================= UTILS ================= */

function clamp(v,min,max){

    return Math.max(
        min,
        Math.min(max,v)
    );
}

function dist(a,b){

    return Math.hypot(
        a.x-b.x,
        a.y-b.y
    );
}

function rand(min,max){

    return Math.random() *
        (max-min) + min;
}

/* ================= PARTICLES ================= */

function particle(
    x,
    y,
    color,
    amount=8,
    power=180
){

    for(let i=0;i<amount;i++){

        const a =
            Math.random() *
            Math.PI*2;

        const sp =
            Math.random() *
            power;

        particles.push({

            x:x,
            y:y,

            vx:Math.cos(a)*sp,
            vy:Math.sin(a)*sp,

            life:rand(.25,.7),
            maxLife:.7,

            size:rand(2,6),

            color:color
        });
    }
}

function updateParticles(dt){

    for(
        let i=particles.length-1;
        i>=0;
        i--
    ){

        const p =
            particles[i];

        p.x += p.vx*dt;
        p.y += p.vy*dt;

        p.vy += 250*dt;

        p.life -= dt;

        if(p.life<=0){

            particles.splice(i,1);
        }
    }
}

function drawParticles(){

    for(const p of particles){

        ctx.globalAlpha =
            Math.max(
                0,
                p.life/p.maxLife
            );

        ctx.fillStyle = p.color;

        ctx.beginPath();

        ctx.arc(
            p.x,
            p.y,
            p.size,
            0,
            Math.PI*2
        );

        ctx.fill();
    }

    ctx.globalAlpha = 1;
}

/* ================= EFFECTS ================= */

function ring(
    x,
    y,
    color,
    size=50
){

    effects.push({

        type:"ring",
        x:x,
        y:y,
        color:color,
        size:size,
        life:.35,
        maxLife:.35
    });
}

function slashEffect(
    x,
    y,
    color,
    dir
){

    effects.push({

        type:"slash",
        x:x,
        y:y,
        color:color,
        dir:dir,
        life:.25,
        maxLife:.25
    });
}

function updateEffects(dt){

    for(
        let i=effects.length-1;
        i>=0;
        i--
    ){

        effects[i].life -= dt;

        if(effects[i].life<=0){

            effects.splice(i,1);
        }
    }
}

function drawEffects(){

    for(const e of effects){

        const alpha =
            e.life/e.maxLife;

        ctx.globalAlpha = alpha;

        if(e.type==="ring"){

            ctx.strokeStyle=e.color;
            ctx.lineWidth=5;

            ctx.beginPath();

            ctx.arc(
                e.x,
                e.y,
                e.size *
                (1-alpha),
                0,
                Math.PI*2
            );

            ctx.stroke();

        }else if(e.type==="slash"){

            ctx.strokeStyle=e.color;
            ctx.lineWidth=10;
            ctx.lineCap="round";

            ctx.beginPath();

            ctx.moveTo(
                e.x - 50*e.dir,
                e.y + 25
            );

            ctx.quadraticCurveTo(
                e.x,
                e.y - 45,
                e.x + 55*e.dir,
                e.y - 8
            );

            ctx.stroke();
        }
    }

    ctx.globalAlpha=1;
}

/* ================= PROJECTILES ================= */

function createProjectile(
    owner,
    style
){

    const dir =
        owner.facing;

    let color =
        CHARACTERS[
            owner.charKey
        ].color;

    let speed = 590;

    if(style==="thunder"){
        speed=850;
    }

    if(style==="wind"){
        speed=780;
    }

    if(style==="fire"){
        speed=650;
    }

    projectiles.push({

        x:owner.x + dir*65,

        y:owner.y - 50,

        vx:dir*speed,

        vy:style==="wind"
            ? Math.sin(performance.now()/100)*25
            : 0,

        owner:owner,

        style:style,

        color:color,

        life:2,

        radius:
            style==="wind"
            ? 18
            : 15,

        damage:
            owner.charKey==="rock"
            ? 18
            : owner.charKey==="thunder"
            ? 17
            : owner.charKey==="wind"
            ? 16
            : 15
    });

    sfxSkill(style);
}

function updateProjectiles(dt){

    for(
        let i=projectiles.length-1;
        i>=0;
        i--
    ){

        const p =
            projectiles[i];

        p.x += p.vx*dt;
        p.y += p.vy*dt;

        if(p.style==="wind"){

            p.y +=
                Math.sin(
                    performance.now()/120
                ) * .7;
        }

        p.life -= dt;

        const target =
            p.owner === p1
            ? p2
            : p1;

        if(
            target &&
            !target.dead &&
            Math.abs(p.x-target.x)<55 &&
            Math.abs(p.y-(target.y-45))<75
        ){

            target.takeDamage(
                p.damage,
                p.owner,
                false
            );

            particle(
                target.x,
                target.y-45,
                p.color,
                12,
                190
            );

            ring(
                target.x,
                target.y-45,
                p.color,
                55
            );

            projectiles.splice(i,1);

            continue;
        }

        if(
            p.life<=0 ||
            p.x<-100 ||
            p.x>W+100
        ){

            projectiles.splice(i,1);
        }
    }
}

function drawProjectile(p){

    ctx.save();

    ctx.translate(
        p.x,
        p.y
    );

    const angle =
        Math.atan2(
            p.vy,
            p.vx
        );

    ctx.rotate(angle);

    if(p.style==="water"){

        ctx.shadowBlur=25;
        ctx.shadowColor="#36c8ff";

        ctx.fillStyle="#76e7ff";

        ctx.beginPath();

        ctx.ellipse(
            0,
            0,
            38,
            15,
            0,
            0,
            Math.PI*2
        );

        ctx.fill();

    }else if(p.style==="fire"){

        ctx.shadowBlur=30;
        ctx.shadowColor="#ff4422";

        ctx.fillStyle="#ff8b2f";

        ctx.beginPath();

        ctx.moveTo(42,0);
        ctx.quadraticCurveTo(
            0,-20,
            -30,0
        );
        ctx.quadraticCurveTo(
            0,20,
            42,0
        );

        ctx.fill();

    }else if(p.style==="thunder"){

        ctx.shadowBlur=30;
        ctx.shadowColor="#fff06a";

        ctx.strokeStyle="#fff9a3";
        ctx.lineWidth=7;

        ctx.beginPath();

        ctx.moveTo(-25,0);
        ctx.lineTo(-5,-18);
        ctx.lineTo(5,4);
        ctx.lineTo(22,-15);
        ctx.lineTo(35,0);

        ctx.stroke();

    }else if(p.style==="flower"){

        ctx.fillStyle="#ff9cdd";

        for(let i=0;i<5;i++){

            const a =
                i*Math.PI*2/5;

            ctx.beginPath();

            ctx.ellipse(
                Math.cos(a)*14,
                Math.sin(a)*14,
                13,
                7,
                a,
                0,
                Math.PI*2
            );

            ctx.fill();
        }

        ctx.fillStyle="#fff0a4";

        ctx.beginPath();

        ctx.arc(
            0,
            0,
            7,
            0,
            Math.PI*2
        );

        ctx.fill();

    }else if(p.style==="rock"){

        ctx.fillStyle="#cdbf9d";

        ctx.beginPath();

        ctx.moveTo(30,0);
        ctx.lineTo(10,-18);
        ctx.lineTo(-25,-12);
        ctx.lineTo(-35,12);
        ctx.lineTo(5,20);

        ctx.closePath();
        ctx.fill();

    }else if(p.style==="wind"){

        ctx.shadowBlur=35;
        ctx.shadowColor="#75ffe0";

        ctx.strokeStyle="#cffff4";
        ctx.lineWidth=8;

        ctx.beginPath();

        ctx.arc(
            0,
            0,
            35,
            -1.1,
            1.1
        );

        ctx.stroke();

        ctx.strokeStyle="#5ff0c9";
        ctx.lineWidth=4;

        ctx.beginPath();

        ctx.arc(
            10,
            0,
            23,
            -.9,
            .9
        );

        ctx.stroke();
    }

    ctx.restore();
}

/* ================= FIGHTER ================= */

class Fighter{

    constructor(
        x,
        side,
        charKey
    ){

        this.x=x;

        this.y=FLOOR_Y;

        this.vx=0;
        this.vy=0;

        this.side=side;

        this.charKey=charKey;

        this.data=
            CHARACTERS[charKey];

        this.hp=100;
        this.energy=0;

        this.facing =
            side===1
            ? 1
            : -1;

        this.width=60;
        this.height=115;

        this.onGround=true;

        this.attackCooldown=0;
        this.skillCooldown=0;
        this.heavyCooldown=0;
        this.dashCooldown=0;
        this.ultimateCooldown=0;

        this.attackTimer=0;
        this.heavyTimer=0;
        this.ultimateTimer=0;

        this.combo=0;
        this.comboTimer=0;

        this.dashTimer=0;
        this.invincible=0;

        this.hitStun=0;

        this.flash=0;

        this.dead=false;

        this.cpuThink=0;

        this.cpuMove=0;
        this.cpuJumpTimer=0;
    }

    updateTimers(dt){

        this.attackCooldown =
            Math.max(
                0,
                this.attackCooldown-dt
            );

        this.skillCooldown =
            Math.max(
                0,
                this.skillCooldown-dt
            );

        this.heavyCooldown =
            Math.max(
                0,
                this.heavyCooldown-dt
            );

        this.dashCooldown =
            Math.max(
                0,
                this.dashCooldown-dt
            );

        this.ultimateCooldown =
            Math.max(
                0,
                this.ultimateCooldown-dt
            );

        this.attackTimer =
            Math.max(
                0,
                this.attackTimer-dt
            );

        this.heavyTimer =
            Math.max(
                0,
                this.heavyTimer-dt
            );

        this.ultimateTimer =
            Math.max(
                0,
                this.ultimateTimer-dt
            );

        this.dashTimer =
            Math.max(
                0,
                this.dashTimer-dt
            );

        this.invincible =
            Math.max(
                0,
                this.invincible-dt
            );

        this.hitStun =
            Math.max(
                0,
                this.hitStun-dt
            );

        this.flash =
            Math.max(
                0,
                this.flash-dt
            );

        if(this.comboTimer>0){

            this.comboTimer-=dt;

        }else{

            this.combo=0;
        }
    }

    update(dt){

        if(this.dead) return;

        this.updateTimers(dt);

        /* ================= ENERGY ================= */

        this.energy =
            clamp(
                this.energy + 8*dt,
                0,
                100
            );

        /* ================= CPU ================= */

        if(this.side===2 && mode==="cpu"){

            this.cpuUpdate(dt);
        }

        if(this.hitStun<=0){

            this.moveUpdate(dt);
        }

        /* ================= GRAVITY ================= */

        this.vy += 1450*dt;

        /* HARD LIMIT:
           Không bao giờ cho vận tốc Y
           tăng vô hạn.
        */

        this.vy =
            clamp(
                this.vy,
                -580,
                950
            );

        this.y += this.vy*dt;

        /* ================= FLOOR ================= */

        if(this.y>=FLOOR_Y){

            this.y=FLOOR_Y;

            this.vy=0;

            this.onGround=true;

        }else{

            this.onGround=false;
        }

        /* ================= WORLD LIMIT ================= */

        this.x =
            clamp(
                this.x,
                65,
                W-65
            );

        /*
         * Nếu vì bất kỳ lý do gì nhân vật
         * lọt khỏi vùng an toàn thì kéo
         * ngay về sân.
         */

        if(!Number.isFinite(this.x)){
            this.x =
                this.side===1
                ? W*.28
                : W*.72;
        }

        if(!Number.isFinite(this.y)){
            this.y=FLOOR_Y;
            this.vy=0;
        }

        this.vx =
            clamp(
                this.vx,
                -420,
                420
            );

        /* ================= DASH ================= */

        if(this.dashTimer>0){

            this.x +=
                this.facing *
                1200 *
                dt;

            this.x =
                clamp(
                    this.x,
                    65,
                    W-65
                );

            if(
                Math.random()<.8
            ){

                afterimages.push({

                    x:this.x,
                    y:this.y,
                    color:this.data.color,
                    life:.18
                });
            }
        }

        /* ================= FRICTION ================= */

        if(
            this.dashTimer<=0 &&
            this.hitStun<=0
        ){

            this.vx *=
                Math.pow(
                    .0008,
                    dt
                );
        }
    }

    moveUpdate(dt){

        let left=false;
        let right=false;
        let jump=false;
        let fall=false;

        if(this.side===1){

            left=!!keys["a"];
            right=!!keys["d"];
            jump=!!keys["w"];
            fall=!!keys["s"];

        }else if(mode==="1v1"){

            left=!!keys["arrowleft"];
            right=!!keys["arrowright"];
            jump=!!keys["arrowup"];
            fall=!!keys["arrowdown"];
        }

        const accel=1500;
        const maxSpeed=285;

        if(left){

            this.vx -= accel*dt;
            this.facing=-1;

        }else if(right){

            this.vx += accel*dt;
            this.facing=1;
        }

        this.vx =
            clamp(
                this.vx,
                -maxSpeed,
                maxSpeed
            );

        if(
            jump &&
            this.onGround
        ){

            this.vy=-580;
            this.onGround=false;

            sfxJump();

            particle(
                this.x,
                this.y,
                this.data.color,
                8,
                120
            );
        }

        if(
            fall &&
            !this.onGround
        ){

            this.vy =
                Math.min(
                    this.vy+1000*dt,
                    950
                );
        }
    }

    cpuUpdate(dt){

        const target=p1;

        if(!target) return;

        this.cpuThink-=dt;

        if(this.cpuThink<=0){

            this.cpuThink=
                rand(.08,.22);

            const dx=
                target.x-this.x;

            const adx=
                Math.abs(dx);

            this.cpuMove =
                adx>150
                ? Math.sign(dx)
                : 0;

            if(
                Math.random()<.16 &&
                this.onGround &&
                adx<450
            ){

                this.cpuJumpTimer=.12;
            }

            if(
                adx<125 &&
                Math.random()<.45
            ){

                this.attack();
            }

            if(
                adx<280 &&
                this.energy>=25 &&
                Math.random()<.28
            ){

                this.skill();
            }

            if(
                adx<155 &&
                this.energy>=10 &&
                Math.random()<.16
            ){

                this.heavy();
            }

            if(
                adx<310 &&
                this.energy>=100 &&
                Math.random()<.10
            ){

                this.ultimate();
            }

            if(
                adx>180 &&
                adx<500 &&
                Math.random()<.16
            ){

                this.dash();
            }
        }

        if(this.cpuMove<0){

            this.vx -=
                1500*dt;

            this.facing=-1;

        }else if(this.cpuMove>0){

            this.vx +=
                1500*dt;

            this.facing=1;
        }

        this.vx =
            clamp(
                this.vx,
                -285,
                285
            );

        if(this.cpuJumpTimer>0){

            this.cpuJumpTimer-=dt;

            if(this.onGround){

                this.vy=-580;
                this.onGround=false;
            }
        }
    }

    attack(){

        if(
            this.dead ||
            this.attackCooldown>0 ||
            this.hitStun>0
        ) return;

        this.attackCooldown=.30;
        this.attackTimer=.18;

        this.combo++;

        if(this.combo>3){
            this.combo=1;
        }

        this.comboTimer=.65;

        const damage =
            this.combo===3
            ? 9
            : 7;

        const target =
            this===p1
            ? p2
            : p1;

        if(
            target &&
            !target.dead &&
            Math.abs(
                target.x-this.x
            )<=108 &&
            Math.abs(
                target.y-this.y
            )<130 &&
            Math.sign(
                target.x-this.x
            )===this.facing
        ){

            target.takeDamage(
                damage,
                this,
                false
            );
        }

        slashEffect(
            this.x+
                this.facing*65,
            this.y-60,
            this.data.color,
            this.facing
        );

        particle(
            this.x+
                this.facing*70,
            this.y-55,
            this.data.color,
            5,
            110
        );

        sfxSlash();
    }

    skill(){

        if(
            this.dead ||
            this.energy<25 ||
            this.skillCooldown>0 ||
            this.hitStun>0
        ) return;

        this.energy-=25;
        this.skillCooldown=1;

        createProjectile(
            this,
            this.data.style
        );

        ring(
            this.x+
                this.facing*45,
            this.y-55,
            this.data.color,
            35
        );
    }

    dash(){

        if(
            this.dead ||
            this.dashCooldown>0 ||
            this.hitStun>0
        ) return;

        this.dashCooldown=.7;
        this.dashTimer=.19;
        this.invincible=.19;

        sfxDash(
            this.data.style
        );

        particle(
            this.x,
            this.y-40,
            this.data.color,
            15,
            220
        );
    }

    heavy(){

        if(
            this.dead ||
            this.heavyCooldown>0 ||
            this.hitStun>0
        ) return;

        this.heavyCooldown=.72;
        this.heavyTimer=.30;

        const target =
            this===p1
            ? p2
            : p1;

        if(
            target &&
            !target.dead &&
            Math.abs(
                target.x-this.x
            )<=135 &&
            Math.abs(
                target.y-this.y
            )<135 &&
            Math.sign(
                target.x-this.x
            )===this.facing
        ){

            target.takeDamage(
                13,
                this,
                true
            );
        }

        slashEffect(
            this.x+
                this.facing*80,
            this.y-58,
            this.data.accent,
            this.facing
        );

        ring(
            this.x+
                this.facing*80,
            this.y-58,
            this.data.accent,
            65
        );

        sfxHeavy();
    }

    ultimate(){

        if(
            this.dead ||
            this.energy<100 ||
            this.ultimateCooldown>0 ||
            this.hitStun>0
        ) return;

        this.energy=0;

        this.ultimateCooldown=4;
        this.ultimateTimer=.65;

        sfxUltimate(
            this.data.style
        );

        const target =
            this===p1
            ? p2
            : p1;

        if(
            target &&
            !target.dead &&
            Math.abs(
                target.x-this.x
            )<=310 &&
            Math.abs(
                target.y-this.y
            )<170 &&
            Math.sign(
                target.x-this.x
            )===this.facing
        ){

            target.takeDamage(
                32,
                this,
                true
            );
        }

        for(let i=0;i<45;i++){

            particle(
                this.x+
                    rand(-120,120),
                this.y-
                    rand(10,150),
                this.data.color,
                1,
                350
            );
        }

        ring(
            this.x+
                this.facing*120,
            this.y-60,
            this.data.color,
            160
        );

        effects.push({

            type:"ultimate",

            x:this.x,

            y:this.y-65,

            color:this.data.color,

            life:.75,

            maxLife:.75
        });
    }

    /*
     * ============================
     * DAMAGE
     * ============================
     *
     * QUAN TRỌNG:
     *
     * Knockback giờ CHỈ là vận tốc ngang.
     * vy KHÔNG bị cộng lực từ đòn đánh.
     *
     * Đây là phần sửa lỗi nhân vật
     * bị đánh bay lên trời.
     */

    takeDamage(
        damage,
        attacker,
        heavy=false
    ){

        if(
            this.dead ||
            this.invincible>0
        ) return;

        this.hp =
            clamp(
                this.hp-damage,
                0,
                100
            );

        this.flash=.12;

        this.hitStun =
            heavy
            ? .18
            : .11;

        /*
         * Knockback ngang cố định.
         * Không bao giờ sửa vy.
         */

        const direction =
            attacker.x < this.x
            ? 1
            : -1;

        const force =
            heavy
            ? 340
            : 190;

        this.vx =
            clamp(
                direction*force,
                -380,
                380
            );

        /*
         * Tuyệt đối không:
         *
         * this.vy -= ...
         *
         * vì đó là nguyên nhân làm
         * nhân vật bay khỏi sân.
         */

        particle(
            this.x,
            this.y-55,
            attacker.data.color,
            heavy ? 18 : 10,
            heavy ? 250 : 170
        );

        ring(
            this.x,
            this.y-55,
            attacker.data.color,
            heavy ? 75 : 50
        );

        sfxHit();

        if(this.hp<=0){

            this.hp=0;

            this.dead=true;

            this.vx=0;
            this.vy=0;

            for(let i=0;i<35;i++){

                particle(
                    this.x,
                    this.y-55,
                    this.data.color,
                    1,
                    320
                );
            }

            setTimeout(()=>{

                if(gameRunning){
                    endGame(
                        attacker===p1
                        ? 1
                        : 2
                    );
                }

            },350);
        }
    }

    draw(){

        if(this.dead) return;

        const d=this.data;

        ctx.save();

        /* aura */

        ctx.shadowBlur =
            this.charKey==="wind"
            ? 35
            : 24;

        ctx.shadowColor =
            d.color;

        ctx.globalAlpha =
            this.flash>0
            ? .65
            : 1;

        /* ground shadow */

        ctx.save();

        ctx.shadowBlur=18;
        ctx.shadowColor="rgba(0,0,0,.7)";
        ctx.fillStyle="rgba(0,0,0,.42)";

        ctx.beginPath();

        ctx.ellipse(
            this.x,
            FLOOR_Y+2,
            48,
            11,
            0,
            0,
            Math.PI*2
        );

        ctx.fill();

        ctx.restore();

        /* body */

        const bodyTop =
            this.y-105;

        const bodyBottom =
            this.y-15;

        ctx.fillStyle=d.dark;

        ctx.beginPath();

        ctx.roundRect(
            this.x-25,
            bodyTop+28,
            50,
            68,
            15
        );

        ctx.fill();

        /* clothing */

        ctx.fillStyle=d.color;

        ctx.beginPath();

        ctx.moveTo(
            this.x-25,
            bodyTop+35
        );

        ctx.lineTo(
            this.x-38,
            bodyBottom
        );

        ctx.lineTo(
            this.x,
            bodyBottom-13
        );

        ctx.lineTo(
            this.x+38,
            bodyBottom
        );

        ctx.lineTo(
            this.x+25,
            bodyTop+35
        );

        ctx.closePath();

        ctx.fill();

        /* head */

        ctx.fillStyle=d.light;

        ctx.beginPath();

        ctx.arc(
            this.x,
            bodyTop+17,
            25,
            0,
            Math.PI*2
        );

        ctx.fill();

        /* hair */

        ctx.fillStyle=d.dark;

        ctx.beginPath();

        ctx.moveTo(
            this.x-28,
            bodyTop+14
        );

        ctx.quadraticCurveTo(
            this.x-20,
            bodyTop-17,
            this.x,
            bodyTop-10
        );

        ctx.quadraticCurveTo(
            this.x+25,
            bodyTop-17,
            this.x+29,
            bodyTop+13
        );

        ctx.lineTo(
            this.x+15,
            bodyTop+2
        );

        ctx.lineTo(
            this.x+7,
            bodyTop+18
        );

        ctx.lineTo(
            this.x-4,
            bodyTop+1
        );

        ctx.lineTo(
            this.x-17,
            bodyTop+18
        );

        ctx.closePath();

        ctx.fill();

        /* eyes */

        ctx.fillStyle="#091020";

        ctx.beginPath();

        ctx.ellipse(
            this.x+
                this.facing*9,
            bodyTop+18,
            4,
            3,
            0,
            0,
            Math.PI*2
        );

        ctx.fill();

        /* sword */

        this.drawSword();

        /* special wind */

        if(this.charKey==="wind"){

            ctx.save();

            ctx.globalAlpha=.55;

            ctx.strokeStyle="#bffff1";
            ctx.lineWidth=3;

            for(let i=0;i<4;i++){

                ctx.beginPath();

                ctx.arc(
                    this.x+
                        Math.sin(
                            performance.now()/280+i
                        )*12,
                    this.y-60,
                    50+i*13,
                    -1.1,
                    1.2
                );

                ctx.stroke();
            }

            ctx.restore();
        }

        /* flower petals */

        if(this.charKey==="flower"){

            ctx.save();

            ctx.fillStyle="#ff9ddd";

            for(let i=0;i<4;i++){

                const a =
                    performance.now()/600+i*1.7;

                ctx.beginPath();

                ctx.ellipse(
                    this.x+
                        Math.cos(a)*42,
                    this.y-55+
                        Math.sin(a)*35,
                    7,
                    3,
                    a,
                    0,
                    Math.PI*2
                );

                ctx.fill();
            }

            ctx.restore();
        }

        ctx.restore();
    }

    drawSword(){

        const d=this.data;

        ctx.save();

        ctx.translate(
            this.x+
                this.facing*23,
            this.y-50
        );

        ctx.rotate(
            this.facing*
            (this.attackTimer>0
             ? -.8
             : -.35)
        );

        ctx.shadowBlur=15;
        ctx.shadowColor=d.color;

        /* handle */

        ctx.strokeStyle=d.dark;
        ctx.lineWidth=8;

        ctx.beginPath();

        ctx.moveTo(-5,5);
        ctx.lineTo(22,22);

        ctx.stroke();

        /* blade */

        ctx.strokeStyle=d.light;
        ctx.lineWidth=5;

        ctx.beginPath();

        ctx.moveTo(18,18);
        ctx.lineTo(18,-65);

        ctx.stroke();

        ctx.strokeStyle=d.color;
        ctx.lineWidth=2;

        ctx.beginPath();

        ctx.moveTo(22,18);
        ctx.lineTo(22,-65);

        ctx.stroke();

        ctx.restore();
    }
}

/* ================= KEY ACTIONS ================= */

function handlePlayerActions(){

    if(!gameRunning) return;

    if(p1){

        if(keys["j"]){
            p1.attack();
        }

        if(keys["k"]){
            p1.skill();
        }

        if(keys["l"]){
            p1.dash();
        }

        if(keys["u"]){
            p1.heavy();
        }

        if(keys["i"]){
            p1.ultimate();
        }
    }

    if(
        p2 &&
        mode==="1v1"
    ){

        if(keys["1"]){
            p2.attack();
        }

        if(keys["2"]){
            p2.skill();
        }

        if(keys["3"]){
            p2.dash();
        }

        if(keys["4"]){
            p2.heavy();
        }

        if(keys["5"]){
            p2.ultimate();
        }
    }
}

/*
 * Key debounce:
 * tránh giữ phím làm gọi attack
 * hàng nghìn lần mỗi giây.
 */

let previousKeys={};

function processActions(){

    const actionKeys=[
        "j",
        "k",
        "l",
        "u",
        "i",
        "1",
        "2",
        "3",
        "4",
        "5"
    ];

    for(const k of actionKeys){

        const now=!!keys[k];
        const old=!!previousKeys[k];

        if(now && !old){

            if(k==="j" && p1)
                p1.attack();

            if(k==="k" && p1)
                p1.skill();

            if(k==="l" && p1)
                p1.dash();

            if(k==="u" && p1)
                p1.heavy();

            if(k==="i" && p1)
                p1.ultimate();

            if(mode==="1v1" && p2){

                if(k==="1")
                    p2.attack();

                if(k==="2")
                    p2.skill();

                if(k==="3")
                    p2.dash();

                if(k==="4")
                    p2.heavy();

                if(k==="5")
                    p2.ultimate();
            }
        }

        previousKeys[k]=now;
    }
}

/* ================= WORLD ================= */

function drawBackground(){

    const grad =
        ctx.createLinearGradient(
            0,
            0,
            0,
            H
        );

    grad.addColorStop(
        0,
        "#070b24"
    );

    grad.addColorStop(
        .55,
        "#111747"
    );

    grad.addColorStop(
        1,
        "#050713"
    );

    ctx.fillStyle=grad;

    ctx.fillRect(
        0,
        0,
        W,
        H
    );

    /* moon */

    ctx.shadowBlur=40;
    ctx.shadowColor="#a8d9ff";

    ctx.fillStyle="#d9efff";

    ctx.beginPath();

    ctx.arc(
        W*.78,
        120,
        55,
        0,
        Math.PI*2
    );

    ctx.fill();

    ctx.shadowBlur=0;

    /* clouds */

    ctx.fillStyle="rgba(130,160,220,.10)";

    for(let i=0;i<7;i++){

        const x=
            (i*260+
            performance.now()*.01)
            % (W+300)-150;

        const y=
            80+
            (i%3)*65;

        ctx.beginPath();

        ctx.ellipse(
            x,
            y,
            100,
            24,
            0,
            0,
            Math.PI*2
        );

        ctx.fill();
    }

    /* city */

    ctx.fillStyle="#070b1c";

    for(let x=0;x<W;x+=70){

        const bh=
            50+
            ((x*17)%120);

        ctx.fillRect(
            x,
            FLOOR_Y-bh,
            55,
            bh
        );

        ctx.fillStyle=
            "rgba(110,180,255,.10)";

        for(
            let wy=FLOOR_Y-bh+15;
            wy<FLOOR_Y-10;
            wy+=22
        ){

            ctx.fillRect(
                x+10,
                wy,
                7,
                5
            );

            ctx.fillRect(
                x+28,
                wy,
                7,
                5
            );
        }

        ctx.fillStyle="#070b1c";
    }

    /* arena floor */

    ctx.fillStyle="#090d1c";

    ctx.fillRect(
        0,
        FLOOR_Y,
        W,
        H-FLOOR_Y
    );

    /* grid */

    ctx.strokeStyle=
        "rgba(80,150,255,.12)";

    ctx.lineWidth=1;

    for(
        let x=0;
        x<W;
        x+=70
    ){

        ctx.beginPath();

        ctx.moveTo(
            x,
            FLOOR_Y
        );

        ctx.lineTo(
            x,
            H
        );

        ctx.stroke();
    }

    for(
        let y=FLOOR_Y;
        y<H;
        y+=35
    ){

        ctx.beginPath();

        ctx.moveTo(
            0,
            y
        );

        ctx.lineTo(
            W,
            y
        );

        ctx.stroke();
    }

    /* center line */

    ctx.strokeStyle=
        "rgba(120,220,255,.22)";

    ctx.lineWidth=2;

    ctx.beginPath();

    ctx.moveTo(
        W/2,
        FLOOR_Y
    );

    ctx.lineTo(
        W/2,
        H
    );

    ctx.stroke();
}

/* ================= AFTERIMAGES ================= */

function updateAfterimages(dt){

    for(
        let i=afterimages.length-1;
        i>=0;
        i--
    ){

        afterimages[i].life-=dt;

        if(afterimages[i].life<=0){

            afterimages.splice(i,1);
        }
    }
}

function drawAfterimages(){

    for(const a of afterimages){

        ctx.globalAlpha =
            a.life/.18*.25;

        ctx.fillStyle=a.color;

        ctx.beginPath();

        ctx.arc(
            a.x,
            a.y-60,
            35,
            0,
            Math.PI*2
        );

        ctx.fill();
    }

    ctx.globalAlpha=1;
}

/* ================= ULTIMATE EFFECT ================= */

function drawUltimateEffects(){

    for(const e of effects){

        if(e.type!=="ultimate")
            continue;

        const alpha =
            e.life/e.maxLife;

        ctx.save();

        ctx.globalAlpha =
            alpha*.65;

        ctx.strokeStyle=e.color;

        ctx.lineWidth=10;

        ctx.shadowBlur=40;
        ctx.shadowColor=e.color;

        ctx.beginPath();

        ctx.arc(
            e.x,
            e.y,
            100+
                (1-alpha)*260,
            0,
            Math.PI*2
        );

        ctx.stroke();

        if(
            p1 &&
            p1.charKey==="wind" &&
            e.color===
                CHARACTERS.wind.color
        ){

            for(let i=0;i<10;i++){

                const a =
                    performance.now()/300+
                    i*.65;

                ctx.beginPath();

                ctx.arc(
                    e.x+
                        Math.cos(a)*120,
                    e.y+
                        Math.sin(a)*90,
                    50+i*8,
                    a,
                    a+1.2
                );

                ctx.stroke();
            }
        }

        ctx.restore();
    }
}

/* ================= DRAW ================= */

function draw(){

    drawBackground();

    drawAfterimages();

    for(const p of projectiles){

        drawProjectile(p);
    }

    if(p1) p1.draw();
    if(p2) p2.draw();

    drawParticles();
    drawEffects();
    drawUltimateEffects();
}

/* ================= HUD ================= */

function updateHUD(){

    if(!p1 || !p2) return;

    document.getElementById(
        "p1Hp"
    ).style.width =
        p1.hp+"%";

    document.getElementById(
        "p2Hp"
    ).style.width =
        p2.hp+"%";

    document.getElementById(
        "p1Energy"
    ).style.width =
        p1.energy+"%";

    document.getElementById(
        "p2Energy"
    ).style.width =
        p2.energy+"%";

    document.getElementById(
        "timer"
    ).textContent =
        Math.ceil(timeLeft);
}

/* ================= GAME LOOP ================= */

function gameLoop(now){

    if(!lastTime){
        lastTime=now;
    }

    let dt=
        (now-lastTime)/1000;

    lastTime=now;

    dt=
        clamp(
            dt,
            0,
            .033
        );

    if(gameRunning){

        processActions();

        p1.update(dt);
        p2.update(dt);

        updateProjectiles(dt);
        updateParticles(dt);
        updateEffects(dt);
        updateAfterimages(dt);

        timeLeft-=dt;

        if(timeLeft<=0){

            timeLeft=0;

            if(
                p1.hp >
                p2.hp
            ){

                endGame(1);

            }else if(
                p2.hp >
                p1.hp
            ){

                endGame(2);

            }else{

                endGame(0);
            }
        }

        updateHUD();
    }

    draw();

    requestAnimationFrame(
        gameLoop
    );
}

/* ================= COUNTDOWN ================= */

function countdown(){

    countdownRunning=true;

    const el=
        document.getElementById(
            "countdown"
        );

    el.classList.remove(
        "hidden"
    );

    const nums=[
        "3",
        "2",
        "1",
        "FIGHT!"
    ];

    let i=0;

    el.textContent=nums[i];

    sfxCountdown(3);

    const interval=
        setInterval(()=>{

            i++;

            if(i>=nums.length){

                clearInterval(
                    interval
                );

                sfxFight();

                setTimeout(()=>{

                    el.classList.add(
                        "hidden"
                    );

                    countdownRunning=false;
                    gameRunning=true;

                },500);

                return;
            }

            el.textContent=
                nums[i];

            if(nums[i]==="2"){

                sfxCountdown(2);

            }else if(
                nums[i]==="1"
            ){

                sfxCountdown(1);
            }

        },650);
}

/* ================= BALLOONS ================= */

function createBalloons(){

    const colors=[
        "#ff5f7e",
        "#65dfff",
        "#ffe15b",
        "#a876ff",
        "#6ff5d0",
        "#ff87d9"
    ];

    for(let i=0;i<55;i++){

        const b=
            document.createElement(
                "div"
            );

        b.className="balloon";

        b.style.left=
            Math.random()*100+"vw";

        b.style.background=
            colors[
                Math.floor(
                    Math.random()*
                    colors.length
                )
            ];

        b.style.animationDuration=
            (4+
            Math.random()*5)+"s";

        b.style.animationDelay=
            (Math.random()*2)+"s";

        document.body.appendChild(b);

        setTimeout(()=>{

            b.remove();

        },9000);
    }
}

/* ================= END GAME ================= */

function endGame(winner){

    if(!gameRunning) return;

    gameRunning=false;

    const result=
        document.getElementById(
            "result"
        );

    const title=
        document.getElementById(
            "resultTitle"
        );

    const text=
        document.getElementById(
            "resultText"
        );

    result.classList.remove(
        "hidden"
    );

    if(winner===0){

        title.textContent="DRAW";

        text.textContent=
            "⚡ Trận đấu kết thúc với kết quả hòa.";

    }else if(winner===1){

        title.textContent=
            "🏆 VICTORY";

        text.textContent=
            "🎉 Chúc mừng " +
            document.getElementById(
                "p1NameHud"
            ).textContent +
            " đã chiến thắng!";

        createBalloons();

        sfxVictory();

    }else{

        title.textContent=
            "💥 DEFEAT";

        text.textContent=
            "😢 " +
            document.getElementById(
                "p1NameHud"
            ).textContent +
            " đã thua trận.";

        sfxDefeat();
    }
}

/* ================= START GAME ================= */

function startGame(){

    initAudio();

    const p1Name =
        document.getElementById(
            "p1NameInput"
        ).value.trim() ||
        "PLAYER 1";

    let p2Name =
        document.getElementById(
            "p2NameInput"
        ).value.trim() ||
        "PLAYER 2";

    if(mode==="cpu"){
        p2Name="MÁY";
    }

    if(
        mode==="cpu" &&
        selectedP2===selectedP1
    ){

        const available=
            charKeys.filter(
                x=>x!==selectedP1
            );

        selectedP2=
            available[
                Math.floor(
                    Math.random()*
                    available.length
                )
            ];
    }

    p1=
        new Fighter(
            W*.28,
            1,
            selectedP1
        );

    p2=
        new Fighter(
            W*.72,
            2,
            selectedP2
        );

    projectiles=[];
    particles=[];
    effects=[];
    afterimages=[];

    timeLeft=60;

    gameRunning=false;
    gameStarted=true;

    document.getElementById(
        "p1NameHud"
    ).textContent=
        p1Name;

    document.getElementById(
        "p2NameHud"
    ).textContent=
        p2Name;

    document.getElementById(
        "p1CharInfo"
    ).textContent=
        CHARACTERS[selectedP1].name+
        " • "+
        CHARACTERS[selectedP1].element;

    document.getElementById(
        "p2CharInfo"
    ).textContent=
        CHARACTERS[selectedP2].name+
        " • "+
        CHARACTERS[selectedP2].element;

    document.getElementById(
        "home"
    ).classList.add(
        "hidden"
    );

    document.getElementById(
        "game"
    ).classList.remove(
        "hidden"
    );

    document.getElementById(
        "result"
    ).classList.add(
        "hidden"
    );

    updateHUD();

    lastTime=0;

    countdown();
}

/* ================= RESET ================= */

function resetGame(){

    document.getElementById(
        "result"
    ).classList.add(
        "hidden"
    );

    startGame();
}

function goHome(){

    gameRunning=false;
    gameStarted=false;

    p1=null;
    p2=null;

    projectiles=[];
    particles=[];
    effects=[];
    afterimages=[];

    document.getElementById(
        "game"
    ).classList.add(
        "hidden"
    );

    document.getElementById(
        "home"
    ).classList.remove(
        "hidden"
    );

    document.querySelectorAll(
        ".balloon"
    ).forEach(
        b=>b.remove()
    );
}

/* ================= MODE ================= */

document.getElementById(
    "mode1v1"
).addEventListener(
    "click",
    ()=>{

        mode="1v1";

        document.getElementById(
            "mode1v1"
        ).classList.add(
            "active"
        );

        document.getElementById(
            "modeCPU"
        ).classList.remove(
            "active"
        );

        document.getElementById(
            "p2NameBox"
        ).classList.remove(
            "hidden"
        );
    }
);

document.getElementById(
    "modeCPU"
).addEventListener(
    "click",
    ()=>{

        mode="cpu";

        document.getElementById(
            "modeCPU"
        ).classList.add(
            "active"
        );

        document.getElementById(
            "mode1v1"
        ).classList.remove(
            "active"
        );

        document.getElementById(
            "p2NameBox"
        ).classList.add(
            "hidden"
        );
    }
);

/* ================= CHARACTER SELECT ================= */

document.querySelectorAll(
    ".char-card"
).forEach(card=>{

    card.addEventListener(
        "click",
        ()=>{

            const key=
                card.dataset.char;

            selectedP1=key;

            document.querySelectorAll(
                ".char-card"
            ).forEach(c=>{

                c.classList.remove(
                    "p1-selected"
                );
            });

            card.classList.add(
                "p1-selected"
            );
        }
    );

    card.addEventListener(
        "dblclick",
        ()=>{

            if(mode!=="1v1") return;

            const key=
                card.dataset.char;

            if(key===selectedP1){

                const available=
                    charKeys.filter(
                        x=>x!==selectedP1
                    );

                selectedP2=
                    available[0];

            }else{

                selectedP2=key;
            }

            document.querySelectorAll(
                ".char-card"
            ).forEach(c=>{

                c.classList.remove(
                    "p2-selected"
                );
            });

            card.classList.add(
                "p2-selected"
            );
        }
    );
});

/* ================= BUTTONS ================= */

document.getElementById(
    "startBtn"
).addEventListener(
    "click",
    startGame
);

document.getElementById(
    "againBtn"
).addEventListener(
    "click",
    resetGame
);

document.getElementById(
    "homeBtn"
).addEventListener(
    "click",
    goHome
);

/* ================= INITIAL ================= */

requestAnimationFrame(
    gameLoop
);

</script>
</body>
</html>
"""

components.html(
    HTML,
    height=1250,
    scrolling=True
)
