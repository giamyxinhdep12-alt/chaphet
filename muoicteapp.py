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
    margin:0;
    padding:0;
}

html,body{
    width:100%;
    height:100%;
    overflow:hidden;
    background:#050711;
    font-family:Arial,Helvetica,sans-serif;
}

body{
    display:flex;
    justify-content:center;
    align-items:center;
}

#gameWrap{
    position:relative;
    width:100%;
    max-width:1500px;
    height:900px;
    overflow:hidden;
    background:#050711;
    border:1px solid rgba(120,160,255,.30);
    border-radius:20px;
    box-shadow:
        0 0 40px rgba(70,110,255,.22),
        inset 0 0 60px rgba(0,0,0,.50);
}

canvas{
    position:absolute;
    inset:0;
    width:100%;
    height:100%;
    display:block;
}

.hidden{
    display:none !important;
}

/* =====================================================
   HOME
===================================================== */

#home{
    position:absolute;
    inset:0;
    z-index:20;
    display:flex;
    flex-direction:column;
    align-items:center;
    padding:25px 28px;
    overflow-y:auto;

    background:
        radial-gradient(
            circle at 50% 15%,
            rgba(75,115,255,.20),
            transparent 34%
        ),
        radial-gradient(
            circle at 10% 70%,
            rgba(100,50,255,.10),
            transparent 30%
        ),
        linear-gradient(
            180deg,
            rgba(5,7,18,.93),
            rgba(6,8,21,.99)
        );
}

.logo{
    font-size:58px;
    font-weight:1000;
    letter-spacing:9px;
    color:white;
    text-align:center;

    text-shadow:
        0 0 8px #72c8ff,
        0 0 25px #477bff,
        0 0 55px rgba(70,100,255,.8);
}

.subtitle{
    margin-top:4px;
    color:#a9b9e9;
    font-size:14px;
    letter-spacing:5px;
    font-weight:900;
}

.homeGrid{
    width:min(1250px,100%);
    display:grid;
    grid-template-columns:1fr 1.35fr;
    gap:20px;
    margin-top:22px;
}

.panel{
    background:
        linear-gradient(
            145deg,
            rgba(20,27,58,.92),
            rgba(7,10,27,.96)
        );

    border:1px solid rgba(130,160,255,.30);
    border-radius:20px;
    padding:20px;

    box-shadow:
        0 10px 35px rgba(0,0,0,.35),
        inset 0 0 35px rgba(70,100,200,.06);
}

.panelTitle{
    color:#eaf0ff;
    font-size:20px;
    font-weight:1000;
    letter-spacing:2px;
    margin-bottom:14px;
}

.inputLabel{
    color:#9aa9d3;
    font-size:14px;
    font-weight:900;
    margin-bottom:6px;
}

input{
    width:100%;
    border:none;
    outline:none;
    border-radius:11px;
    padding:13px 14px;
    color:white;
    background:#0b1027;
    border:1px solid rgba(120,150,255,.28);
    font-weight:800;
    font-size:16px;
}

input:focus{
    border-color:#62bfff;
    box-shadow:0 0 15px rgba(80,170,255,.25);
}

.modeRow{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:11px;
}

.modeBtn{
    border:1px solid rgba(130,160,255,.30);
    background:#0a0f26;
    color:#aebce9;
    border-radius:13px;
    padding:15px 8px;
    cursor:pointer;
    font-weight:1000;
    font-size:16px;
    transition:.2s;
}

.modeBtn:hover{
    transform:translateY(-2px);
    border-color:#6bc5ff;
}

.modeBtn.active{
    color:white;
    background:
        linear-gradient(
            135deg,
            #153b76,
            #251a68
        );

    border-color:#62c7ff;

    box-shadow:
        0 0 20px rgba(80,180,255,.25);
}

#p2Box{
    margin-top:14px;
}

.charGrid{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:11px;
}

.charBtn{
    position:relative;
    min-height:135px;
    border-radius:15px;
    padding:12px 8px;
    cursor:pointer;
    color:white;

    border:1px solid rgba(130,160,255,.20);

    background:
        linear-gradient(
            145deg,
            #10152e,
            #090c1d
        );

    overflow:hidden;
    transition:.2s;
}

.charBtn:hover{
    transform:translateY(-4px);
    border-color:rgba(150,200,255,.8);
}

.charBtn.selected{
    border:2px solid white;
    box-shadow:
        0 0 22px var(--glow),
        inset 0 0 20px rgba(255,255,255,.04);

    transform:translateY(-2px);
}

.charOrb{
    position:relative;
    width:42px;
    height:42px;
    margin:0 auto 8px;
    border-radius:50%;
    background:var(--c);
    box-shadow:
        0 0 12px var(--c),
        0 0 28px var(--c);

    animation:
        orbPulse 1.8s infinite alternate;
}

.charOrb:after{
    content:"";
    position:absolute;
    inset:-8px;
    border-radius:50%;
    border:2px solid var(--c);
    opacity:.25;
    animation:orbRing 2s linear infinite;
}

@keyframes orbPulse{
    from{
        transform:scale(.92);
    }
    to{
        transform:scale(1.08);
    }
}

@keyframes orbRing{
    from{
        transform:scale(.75);
        opacity:.45;
    }
    to{
        transform:scale(1.45);
        opacity:0;
    }
}

.charName{
    font-size:15px;
    font-weight:1000;
}

.charType{
    margin-top:3px;
    font-size:12px;
    color:#aab8de;
    font-weight:900;
}

.charSkill{
    margin-top:7px;
    font-size:10px;
    color:#7382ad;
}

.startBtn{
    width:min(560px,100%);
    margin-top:18px;

    border:0;
    border-radius:15px;

    padding:17px;

    cursor:pointer;

    color:white;
    font-size:19px;
    font-weight:1000;
    letter-spacing:2px;

    background:
        linear-gradient(
            90deg,
            #1479ff,
            #734cff,
            #c94cff
        );

    box-shadow:
        0 0 25px rgba(100,100,255,.40),
        0 8px 25px rgba(0,0,0,.3);

    transition:.2s;
}

.startBtn:hover{
    transform:translateY(-2px) scale(1.015);
    filter:brightness(1.12);
}

/* =====================================================
   GUIDE
===================================================== */

.guideSection{
    width:min(1250px,100%);
    margin-top:18px;
    padding:20px;

    border-radius:18px;

    border:1px solid rgba(110,160,255,.30);

    background:
        linear-gradient(
            145deg,
            rgba(13,20,48,.96),
            rgba(7,10,25,.98)
        );

    box-shadow:
        0 8px 30px rgba(0,0,0,.25);
}

.guideTitle{
    text-align:center;
    color:#76e8ff;
    font-size:25px;
    font-weight:1000;
    letter-spacing:3px;
    margin-bottom:16px;

    text-shadow:
        0 0 12px rgba(90,220,255,.4);
}

.guideGrid{
    display:grid;
    grid-template-columns:1fr 1fr 1fr;
    gap:14px;
}

.guideCard{
    padding:15px;

    border-radius:14px;

    background:#070b18;

    border:1px solid rgba(100,140,220,.22);
}

.guideCard h3{
    color:#e9efff;
    font-size:18px;
    margin-bottom:9px;
}

.guideCard p{
    color:#aebbd9;
    font-size:15px;
    line-height:1.7;
}

.key{
    display:inline-block;
    color:#e7efff;
    background:#111832;
    padding:3px 7px;
    margin:1px;
    border-radius:5px;
    border:1px solid rgba(150,180,255,.18);
    font-weight:1000;
}

/* =====================================================
   SOUND
===================================================== */

.soundBtn{
    position:absolute;
    top:14px;
    left:50%;
    transform:translateX(-50%);
    z-index:40;

    border:1px solid rgba(150,200,255,.35);

    background:rgba(9,14,35,.85);

    color:white;

    border-radius:12px;

    padding:9px 14px;

    cursor:pointer;

    font-weight:900;
    font-size:14px;

    box-shadow:
        0 0 15px rgba(80,150,255,.15);
}

.soundBtn:hover{
    background:#172044;
}

/* =====================================================
   HUD
===================================================== */

#hud{
    position:absolute;
    top:14px;
    left:18px;
    right:18px;
    z-index:10;

    display:flex;
    justify-content:space-between;
    align-items:flex-start;

    pointer-events:none;
}

.hudSide{
    width:38%;
}

.hudSide.right{
    text-align:right;
}

.hudName{
    color:white;
    font-weight:1000;
    font-size:18px;
    text-shadow:0 2px 5px black;
}

.hudHp{
    height:18px;
    margin-top:6px;

    border-radius:20px;
    overflow:hidden;

    background:#080b15;

    border:1px solid rgba(255,255,255,.15);
}

.hpFill{
    height:100%;
    width:100%;

    background:
        linear-gradient(
            90deg,
            #34e88b,
            #b9ff64
        );

    box-shadow:0 0 13px #4aff91;

    transition:.15s;
}

.right .hpFill{
    float:right;

    background:
        linear-gradient(
            90deg,
            #ff6b9a,
            #ff365f
        );

    box-shadow:0 0 13px #ff4c77;
}

.energy{
    height:8px;
    margin-top:5px;

    border-radius:10px;
    overflow:hidden;

    background:#080b15;
}

.energyFill{
    height:100%;
    width:0%;

    background:
        linear-gradient(
            90deg,
            #39b9ff,
            #9c70ff
        );

    box-shadow:0 0 10px #6b9dff;

    transition:.12s;
}

.right .energyFill{
    float:right;
}

.timer{
    min-width:105px;
    text-align:center;

    color:white;

    font-size:32px;
    font-weight:1000;

    text-shadow:
        0 0 12px #7bb9ff;
}

.timer small{
    display:block;

    color:#7583ae;

    font-size:10px;
    letter-spacing:2px;
}

/* =====================================================
   COUNTDOWN
===================================================== */

#countdown{
    position:absolute;
    inset:0;

    z-index:15;

    display:flex;
    justify-content:center;
    align-items:center;

    pointer-events:none;

    font-size:120px;

    color:white;

    font-weight:1000;

    text-shadow:
        0 0 12px #fff,
        0 0 35px #5c9dff,
        0 0 70px #8c4cff;
}

/* =====================================================
   RESULT
===================================================== */

#result{
    position:absolute;
    inset:0;

    z-index:30;

    display:flex;
    flex-direction:column;

    align-items:center;
    justify-content:center;

    background:rgba(3,5,15,.68);

    backdrop-filter:blur(5px);
}

.resultTitle{
    color:white;

    font-size:65px;

    font-weight:1000;

    letter-spacing:5px;

    text-align:center;

    text-shadow:
        0 0 25px #7e9dff,
        0 0 50px rgba(120,100,255,.4);
}

.resultSub{
    color:#c1cdec;

    margin-top:10px;

    font-size:20px;

    font-weight:800;

    text-align:center;
}

.backBtn{
    margin-top:24px;

    border:1px solid rgba(150,190,255,.4);

    background:#111833;

    color:white;

    border-radius:12px;

    padding:14px 28px;

    cursor:pointer;

    font-weight:1000;
    font-size:16px;
}

/* =====================================================
   BALLOONS
===================================================== */

#balloons{
    position:absolute;
    inset:0;

    z-index:29;

    pointer-events:none;

    overflow:hidden;
}

.balloon{
    position:absolute;

    bottom:-90px;

    width:30px;
    height:39px;

    border-radius:50% 50% 48% 48%;

    animation:
        rise 4.5s linear forwards;

    filter:
        drop-shadow(
            0 0 8px currentColor
        );
}

.balloon:after{
    content:"";

    position:absolute;

    width:1px;
    height:65px;

    top:37px;
    left:50%;

    background:rgba(255,255,255,.4);
}

@keyframes rise{
    0%{
        transform:
            translateY(0)
            rotate(-4deg);

        opacity:0;
    }

    10%{
        opacity:1;
    }

    50%{
        transform:
            translateY(-430px)
            translateX(30px)
            rotate(7deg);
    }

    100%{
        transform:
            translateY(-950px)
            translateX(-50px)
            rotate(-8deg);

        opacity:0;
    }
}

#help{
    position:absolute;

    bottom:14px;
    left:50%;

    transform:translateX(-50%);

    z-index:10;

    color:#7887b2;

    font-size:12px;

    white-space:nowrap;

    pointer-events:none;
}

/* =====================================================
   RESPONSIVE
===================================================== */

@media(max-width:1050px){

    #gameWrap{
        height:100vh;
        border-radius:0;
    }

    .homeGrid{
        grid-template-columns:1fr;
    }

    .guideGrid{
        grid-template-columns:1fr;
    }

    .logo{
        font-size:43px;
    }
}

@media(max-width:650px){

    .charGrid{
        grid-template-columns:repeat(2,1fr);
    }

    #home{
        padding:18px 12px;
    }

    .resultTitle{
        font-size:40px;
    }

    #countdown{
        font-size:75px;
    }

    .guideCard p{
        font-size:13px;
    }
}
</style>
</head>

<body>

<div id="gameWrap">

<canvas id="gameCanvas"></canvas>

<!-- =====================================================
     HOME
===================================================== -->

<div id="home">

    <div class="logo">AURA WAR</div>

    <div class="subtitle">
        ⚡ ANIME SWORD ARENA ⚡
    </div>

    <div class="homeGrid">

        <!-- LEFT -->

        <div class="panel">

            <div class="panelTitle">
                ⚔️ TRẬN ĐẤU
            </div>

            <div class="inputLabel">
                TÊN NGƯỜI CHƠI 1
            </div>

            <input
                id="p1Name"
                maxlength="20"
                value="Player 1"
            >

            <div style="height:14px"></div>

            <div class="inputLabel">
                CHẾ ĐỘ
            </div>

            <div class="modeRow">

                <button
                    class="modeBtn active"
                    id="mode1v1"
                >
                    ⚔️ 1V1
                </button>

                <button
                    class="modeBtn"
                    id="modeCPU"
                >
                    🤖 VS MÁY
                </button>

            </div>

            <div id="p2Box">

                <div
                    class="inputLabel"
                    style="margin-top:14px"
                >
                    TÊN NGƯỜI CHƠI 2
                </div>

                <input
                    id="p2Name"
                    maxlength="20"
                    value="Player 2"
                >

            </div>

            <div style="height:20px"></div>

            <div class="panelTitle">
                🎮 ĐIỀU KHIỂN
            </div>

            <div style="
                font-size:14px;
                color:#8290b8;
                line-height:2;
            ">

                <b style="color:#b8c8ed">
                    P1:
                </b>

                <span class="key">A</span>
                <span class="key">D</span>
                di chuyển

                <span class="key">W</span>
                nhảy

                <span class="key">S</span>
                rơi nhanh

                <br>

                <span class="key">J</span>
                đánh

                <span class="key">K</span>
                skill

                <span class="key">L</span>
                dash

                <span class="key">U</span>
                heavy

                <span class="key">I</span>
                ultimate

                <br><br>

                <b style="color:#ff9fdb">
                    P2:
                </b>

                <span class="key">←</span>
                <span class="key">→</span>
                di chuyển

                <span class="key">↑</span>
                nhảy

                <span class="key">↓</span>
                rơi

                <br>

                <span class="key">1</span>
                đánh

                <span class="key">2</span>
                skill

                <span class="key">3</span>
                dash

                <span class="key">4</span>
                heavy

                <span class="key">5</span>
                ultimate

            </div>

        </div>

        <!-- RIGHT -->

        <div class="panel">

            <div class="panelTitle">
                👤 CHỌN NHÂN VẬT
            </div>

            <div class="charGrid">

                <button
                    class="charBtn selected"
                    data-id="water"
                    style="
                        --c:#31bfff;
                        --glow:rgba(40,190,255,.65)
                    "
                >
                    <div class="charOrb"></div>
                    <div class="charName">
                        KAIRO
                    </div>
                    <div class="charType">
                        🌊 THỦY
                    </div>
                    <div class="charSkill">
                        Thủy Long
                    </div>
                </button>

                <button
                    class="charBtn"
                    data-id="fire"
                    style="
                        --c:#ff5a36;
                        --glow:rgba(255,80,40,.65)
                    "
                >
                    <div class="charOrb"></div>
                    <div class="charName">
                        RENJI
                    </div>
                    <div class="charType">
                        🔥 VIÊM
                    </div>
                    <div class="charSkill">
                        Hỏa Lưu
                    </div>
                </button>

                <button
                    class="charBtn"
                    data-id="thunder"
                    style="
                        --c:#ffe44a;
                        --glow:rgba(255,220,50,.65)
                    "
                >
                    <div class="charOrb"></div>
                    <div class="charName">
                        RAI
                    </div>
                    <div class="charType">
                        ⚡ LÔI
                    </div>
                    <div class="charSkill">
                        Lôi Kích
                    </div>
                </button>

                <button
                    class="charBtn"
                    data-id="flower"
                    style="
                        --c:#ff79c8;
                        --glow:rgba(255,100,200,.65)
                    "
                >
                    <div class="charOrb"></div>
                    <div class="charName">
                        MIZUHA
                    </div>
                    <div class="charType">
                        🌸 HOA
                    </div>
                    <div class="charSkill">
                        Hoa Vũ
                    </div>
                </button>

                <button
                    class="charBtn"
                    data-id="rock"
                    style="
                        --c:#b8a98e;
                        --glow:rgba(180,160,120,.60)
                    "
                >
                    <div class="charOrb"></div>
                    <div class="charName">
                        GARO
                    </div>
                    <div class="charType">
                        🪨 ĐÁ
                    </div>
                    <div class="charSkill">
                        Nham Kích
                    </div>
                </button>

                <button
                    class="charBtn"
                    data-id="wind"
                    style="
                        --c:#72f3d0;
                        --glow:rgba(70,255,210,.80)
                    "
                >
                    <div class="charOrb"></div>
                    <div class="charName">
                        KAZE
                    </div>
                    <div class="charType">
                        🌪️ GIÓ
                    </div>
                    <div class="charSkill">
                        Cuồng Phong
                    </div>
                </button>

            </div>

        </div>

    </div>

    <!-- =================================================
         GUIDE BELOW CHARACTER SELECTION
    ================================================== -->

    <div class="guideSection">

        <div class="guideTitle">
            📖 HƯỚNG DẪN CHƠI
        </div>

        <div class="guideGrid">

            <div class="guideCard">

                <h3>
                    ⚔️ Chiến đấu
                </h3>

                <p>
                    HP tối đa:
                    <b style="color:#65ff9b">100</b>
                    <br>

                    Năng lượng tự hồi:
                    <b style="color:#69dfff">8 / giây</b>
                    <br>

                    Đánh thường:
                    <b>7–9 damage</b>
                    <br>

                    Heavy:
                    <b>13 damage</b>
                </p>

            </div>

            <div class="guideCard">

                <h3>
                    💥 Kỹ năng
                </h3>

                <p>
                    Skill cần
                    <b style="color:#69dfff">25 năng lượng</b>.
                    <br>

                    Ultimate cần
                    <b style="color:#ffe66b">100 năng lượng</b>.
                    <br>

                    Dash có thời gian hồi ngắn
                    và có hiệu ứng né đòn.
                </p>

            </div>

            <div class="guideCard">

                <h3>
                    🎮 Phím nhanh
                </h3>

                <p>
                    P1:
                    <span class="key">A</span>
                    <span class="key">D</span>
                    <span class="key">W</span>
                    <span class="key">J</span>
                    <span class="key">K</span>
                    <span class="key">L</span>
                    <span class="key">U</span>
                    <span class="key">I</span>
                    <br>

                    P2:
                    <span class="key">←</span>
                    <span class="key">→</span>
                    <span class="key">↑</span>
                    <span class="key">1</span>
                    <span class="key">2</span>
                    <span class="key">3</span>
                    <span class="key">4</span>
                    <span class="key">5</span>
                </p>

            </div>

        </div>

    </div>

    <button
        class="startBtn"
        id="startBtn"
    >
        ▶ BẮT ĐẦU TRẬN
    </button>

</div>

<!-- =====================================================
     HUD
===================================================== -->

<div
    id="hud"
    class="hidden"
>

    <div class="hudSide">

        <div
            class="hudName"
            id="name1"
        >
            PLAYER 1
        </div>

        <div class="hudHp">
            <div
                class="hpFill"
                id="hp1"
            ></div>
        </div>

        <div class="energy">
            <div
                class="energyFill"
                id="energy1"
            ></div>
        </div>

    </div>

    <div class="timer">

        <small>TIME</small>

        <span id="timer">
            60
        </span>

    </div>

    <div
        class="hudSide right"
    >

        <div
            class="hudName"
            id="name2"
        >
            PLAYER 2
        </div>

        <div class="hudHp">

            <div
                class="hpFill"
                id="hp2"
            ></div>

        </div>

        <div class="energy">

            <div
                class="energyFill"
                id="energy2"
            ></div>

        </div>

    </div>

</div>

<button
    id="soundBtn"
    class="soundBtn"
>
    🔊 ÂM THANH
</button>

<div
    id="countdown"
    class="hidden"
></div>

<div
    id="help"
    class="hidden"
>
    P1:
    A/D W S J K L U I
    &nbsp; • &nbsp;
    P2:
    ← → ↑ ↓ 1 2 3 4 5
</div>

<div id="balloons"></div>

<div
    id="result"
    class="hidden"
>

    <div
        class="resultTitle"
        id="resultTitle"
    >
        VICTORY
    </div>

    <div
        class="resultSub"
        id="resultSub"
    ></div>

    <button
        class="backBtn"
        id="backBtn"
    >
        ↩ VỀ MENU
    </button>

</div>

<script>

/* =========================================================
   CORE
========================================================= */

const canvas=document.getElementById("gameCanvas");
const ctx=canvas.getContext("2d");

let W=1500;
let H=900;

let dpr=Math.min(
    window.devicePixelRatio||1,
    2
);

function resizeCanvas(){

    const rect=canvas.getBoundingClientRect();

    W=rect.width;
    H=rect.height;

    canvas.width=Math.floor(W*dpr);
    canvas.height=Math.floor(H*dpr);

    ctx.setTransform(
        dpr,
        0,
        0,
        dpr,
        0,
        0
    );
}

window.addEventListener(
    "resize",
    resizeCanvas
);

resizeCanvas();

/* =========================================================
   ELEMENTS
========================================================= */

const home=document.getElementById("home");
const hud=document.getElementById("hud");
const countdownEl=document.getElementById("countdown");
const result=document.getElementById("result");
const resultTitle=document.getElementById("resultTitle");
const resultSub=document.getElementById("resultSub");
const balloons=document.getElementById("balloons");
const help=document.getElementById("help");
const soundBtn=document.getElementById("soundBtn");

const mode1v1=document.getElementById("mode1v1");
const modeCPU=document.getElementById("modeCPU");
const p2Box=document.getElementById("p2Box");

const name1El=document.getElementById("name1");
const name2El=document.getElementById("name2");

const hp1El=document.getElementById("hp1");
const hp2El=document.getElementById("hp2");

const energy1El=document.getElementById("energy1");
const energy2El=document.getElementById("energy2");

const timerEl=document.getElementById("timer");

let gameMode="1v1";

let selectedP1="water";
let selectedP2="fire";

/* =========================================================
   AUDIO
========================================================= */

let audioCtx=null;
let masterGain=null;
let soundEnabled=true;

function initAudio(){

    try{

        if(!audioCtx){

            audioCtx=new(
                window.AudioContext||
                window.webkitAudioContext
            )();

            masterGain=
                audioCtx.createGain();

            masterGain.gain.value=.24;

            masterGain.connect(
                audioCtx.destination
            );
        }

        if(
            audioCtx.state===
            "suspended"
        ){
            audioCtx.resume();
        }

    }catch(err){

        soundEnabled=false;
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

    if(
        !audioCtx||
        !masterGain
    ) return;

    const osc=
        audioCtx.createOscillator();

    const g=
        audioCtx.createGain();

    osc.type=type;

    osc.frequency.setValueAtTime(
        freq,
        audioCtx.currentTime
    );

    if(endFreq!==null){

        osc.frequency.exponentialRampToValueAtTime(
            Math.max(30,endFreq),
            audioCtx.currentTime+duration
        );
    }

    g.gain.setValueAtTime(
        .0001,
        audioCtx.currentTime
    );

    g.gain.exponentialRampToValueAtTime(
        gain,
        audioCtx.currentTime+.015
    );

    g.gain.exponentialRampToValueAtTime(
        .0001,
        audioCtx.currentTime+duration
    );

    osc.connect(g);
    g.connect(masterGain);

    osc.start();

    osc.stop(
        audioCtx.currentTime+
        duration+
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

    if(
        !audioCtx||
        !masterGain
    ) return;

    const length=Math.max(
        1,
        Math.floor(
            audioCtx.sampleRate*
            duration
        )
    );

    const buffer=
        audioCtx.createBuffer(
            1,
            length,
            audioCtx.sampleRate
        );

    const data=
        buffer.getChannelData(0);

    for(
        let i=0;
        i<data.length;
        i++
    ){
        data[i]=
            Math.random()*2-1;
    }

    const source=
        audioCtx.createBufferSource();

    const filter=
        audioCtx.createBiquadFilter();

    const g=
        audioCtx.createGain();

    filter.type="bandpass";
    filter.frequency.value=
        filterFreq;

    filter.Q.value=.7;

    g.gain.setValueAtTime(
        gain,
        audioCtx.currentTime
    );

    g.gain.exponentialRampToValueAtTime(
        .0001,
        audioCtx.currentTime+duration
    );

    source.buffer=buffer;

    source.connect(filter);
    filter.connect(g);
    g.connect(masterGain);

    source.start();
}

function sfxSlash(){

    tone(
        480,
        .08,
        "sawtooth",
        .055,
        950
    );

    noise(
        .055,
        .035,
        2800
    );
}

function sfxHeavy(){

    tone(
        120,
        .18,
        "square",
        .10,
        55
    );

    noise(
        .18,
        .12,
        700
    );

    tone(
        260,
        .12,
        "triangle",
        .05,
        80
    );
}

function sfxHit(){

    noise(
        .10,
        .09,
        950
    );

    tone(
        95,
        .10,
        "square",
        .055,
        45
    );
}

function sfxDash(style){

    if(style==="wind"){

        noise(
            .32,
            .075,
            3200
        );

        tone(
            500,
            .28,
            "sine",
            .035,
            1100
        );

    }else{

        noise(
            .18,
            .055,
            2400
        );

        tone(
            240,
            .16,
            "sawtooth",
            .035,
            800
        );
    }
}

function sfxSkill(style){

    if(style==="water"){

        tone(
            330,
            .35,
            "sine",
            .06,
            720
        );

        tone(
            520,
            .30,
            "sine",
            .045,
            980
        );

        noise(
            .16,
            .025,
            1800
        );

    }else if(style==="fire"){

        noise(
            .30,
            .09,
            900
        );

        tone(
            180,
            .25,
            "sawtooth",
            .055,
            70
        );

        tone(
            480,
            .18,
            "triangle",
            .04,
            120
        );

    }else if(style==="thunder"){

        tone(
            900,
            .12,
            "square",
            .07,
            180
        );

        tone(
            1450,
            .08,
            "square",
            .055,
            400
        );

        noise(
            .13,
            .07,
            4200
        );

    }else if(style==="flower"){

        tone(
            520,
            .35,
            "sine",
            .05,
            900
        );

        tone(
            780,
            .42,
            "sine",
            .04,
            1250
        );

    }else if(style==="rock"){

        tone(
            90,
            .32,
            "square",
            .09,
            45
        );

        noise(
            .28,
            .10,
            500
        );

    }else if(style==="wind"){

        noise(
            .55,
            .075,
            3800
        );

        tone(
            420,
            .48,
            "sine",
            .045,
            1200
        );

        tone(
            720,
            .35,
            "triangle",
            .025,
            1450
        );
    }
}

function sfxUltimate(style){

    tone(
        180,
        .30,
        "sine",
        .06,
        420
    );

    tone(
        360,
        .40,
        "sine",
        .055,
        900
    );

    setTimeout(function(){

        if(!soundEnabled) return;

        noise(
            .45,
            .16,
            1100
        );

        tone(
            75,
            .45,
            "square",
            .12,
            35
        );

        tone(
            600,
            .32,
            "sawtooth",
            .065,
            100
        );

        if(style==="wind"){

            noise(
                .65,
                .10,
                4500
            );

            tone(
                900,
                .60,
                "sine",
                .05,
                1600
            );

        }else if(style==="thunder"){

            tone(
                1100,
                .22,
                "square",
                .09,
                120
            );

            noise(
                .35,
                .10,
                5000
            );

        }else if(style==="fire"){

            noise(
                .55,
                .14,
                800
            );

            tone(
                180,
                .40,
                "sawtooth",
                .08,
                45
            );

        }else if(style==="water"){

            tone(
                300,
                .55,
                "sine",
                .07,
                950
            );

            noise(
                .35,
                .05,
                1800
            );

        }else if(style==="rock"){

            tone(
                65,
                .60,
                "square",
                .14,
                30
            );

            noise(
                .55,
                .13,
                450
            );

        }else if(style==="flower"){

            tone(
                600,
                .55,
                "sine",
                .06,
                1300
            );

            tone(
                900,
                .50,
                "sine",
                .04,
                1600
            );

        }

    },260);
}

function sfxJump(){
    tone(
        280,
        .10,
        "sine",
        .035,
        620
    );
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

    noise(
        .12,
        .04,
        3000
    );
}

function sfxVictory(){

    tone(
        523,
        .18,
        "sine",
        .07,
        660
    );

    setTimeout(function(){

        tone(
            659,
            .18,
            "sine",
            .07,
            830
        );

    },140);

    setTimeout(function(){

        tone(
            784,
            .35,
            "sine",
            .09,
            1100
        );

    },280);
}

function sfxDefeat(){

    tone(
        320,
        .25,
        "sine",
        .06,
        220
    );

    setTimeout(function(){

        tone(
            220,
            .40,
            "sine",
            .065,
            100
        );

    },180);
}

function sfxDraw(){

    tone(
        430,
        .18,
        "triangle",
        .05,
        360
    );

    setTimeout(function(){

        tone(
            360,
            .28,
            "triangle",
            .05,
            300
        );

    },160);
}

function toggleSound(){

    soundEnabled=!soundEnabled;

    if(masterGain){

        masterGain.gain.value=
            soundEnabled
            ? .24
            : 0;
    }

    soundBtn.textContent=
        soundEnabled
        ? "🔊 ÂM THANH"
        : "🔇 TẮT ÂM THANH";

    if(soundEnabled){
        initAudio();
    }
}

soundBtn.onclick=toggleSound;

/* =========================================================
   CHARACTER DATA
========================================================= */

const CHARACTERS={

    water:{
        name:"KAIRO",
        element:"THỦY",
        color:"#36c8ff",
        dark:"#1268a4",
        light:"#a7edff",
        accent:"#227aff",
        skillName:"THỦY LONG",
        ultimateName:"HẢI LONG DIỆT",
        projectile:"water",
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
        projectile:"fire",
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
        projectile:"thunder",
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
        projectile:"flower",
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
        projectile:"rock",
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
        projectile:"wind",
        style:"wind"
    }
};

/* =========================================================
   MODE
========================================================= */

mode1v1.onclick=function(){

    gameMode="1v1";

    mode1v1.classList.add("active");
    modeCPU.classList.remove("active");

    p2Box.style.display="block";
};

modeCPU.onclick=function(){

    gameMode="cpu";

    modeCPU.classList.add("active");
    mode1v1.classList.remove("active");

    p2Box.style.display="none";
};

/* =========================================================
   CHARACTER SELECT
========================================================= */

document.querySelectorAll(".charBtn")
.forEach(function(btn){

    btn.onclick=function(){

        if(gameStarted) return;

        const id=btn.dataset.id;

        selectedP1=id;

        document
        .querySelectorAll(".charBtn")
        .forEach(function(x){

            x.classList.remove(
                "selected"
            );

            x.style.outline="";
        });

        btn.classList.add(
            "selected"
        );
    };

    btn.addEventListener(
        "dblclick",
        function(){

            if(gameStarted) return;

            if(gameMode!=="1v1")
                return;

            const id=btn.dataset.id;

            selectedP2=id;

            document
            .querySelectorAll(".charBtn")
            .forEach(function(x){

                x.style.outline="";
            });

            btn.style.outline=
                "2px solid #ff75df";
        }
    );
});

/* =========================================================
   INPUT
========================================================= */

const keys={};

window.addEventListener(
    "keydown",
    function(e){

        const key=
            e.key.toLowerCase();

        keys[key]=true;

        if([
            "arrowleft",
            "arrowright",
            "arrowup",
            "arrowdown",
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
        ]=false;
    }
);

/* =========================================================
   UTILS
========================================================= */

function clamp(v,a,b){

    return Math.max(
        a,
        Math.min(b,v)
    );
}

function rand(a,b){

    return Math.random()*
        (b-a)+a;
}

/* =========================================================
   EFFECT ARRAYS
========================================================= */

const particles=[];
const projectiles=[];
const slashes=[];
const shockwaves=[];
const afterimages=[];
const windBlades=[];
const flowerPetals=[];
const lightningBolts=[];
const fireTrails=[];
const waterArcs=[];
const rockChunks=[];

/* =========================================================
   PARTICLES
========================================================= */

function particle(
    x,
    y,
    color,
    count=10,
    speed=120
){

    for(
        let i=0;
        i<count;
        i++
    ){

        const a=
            Math.random()*
            Math.PI*2;

        const s=
            Math.random()*
            speed;

        particles.push({

            x:x,
            y:y,

            vx:
                Math.cos(a)*s,

            vy:
                Math.sin(a)*s,

            life:
                .45+
                Math.random()*.55,

            max:1,

            size:
                2+
                Math.random()*4,

            color:color
        });
    }
}

function ring(
    x,
    y,
    color,
    size=30
){

    shockwaves.push({

        x:x,
        y:y,

        r:5,

        max:size,

        life:.45,

        color:color
    });
}

function makeAfterimage(f){

    afterimages.push({

        x:f.x,
        y:f.y,

        facing:f.facing,

        color:f.data.color,

        life:.3,

        max:.3,

        style:f.data.style
    });
}

/* =========================================================
   FIGHTER
========================================================= */

class Fighter{

    constructor(x,side,id){

        this.x=x;
        this.y=0;

        this.vx=0;
        this.vy=0;

        this.side=side;
        this.id=id;

        this.data=
            CHARACTERS[id];

        this.hp=100;
        this.energy=0;

        this.width=58;
        this.height=112;

        this.facing=
            side===1
            ?1
            :-1;

        this.grounded=true;

        this.attackTimer=0;
        this.attackCooldown=0;

        this.skillCooldown=0;
        this.dashCooldown=0;
        this.heavyCooldown=0;
        this.ultimateCooldown=0;

        this.dashTimer=0;
        this.dashInvincible=0;

        this.hitFlash=0;
        this.hitStun=0;

        this.state="idle";
        this.anim=0;

        this.combo=0;
        this.comboTimer=0;

        this.dead=false;

        this.cpuThink=0;
        this.cpuMove=0;
        this.cpuJump=false;

        this.cpuAttackDelay=0;
        this.cpuDashDelay=0;
        this.cpuSkillDelay=0;
        this.cpuHeavyDelay=0;
        this.cpuUltDelay=0;
    }

    get floorY(){

        return H-155;
    }

    get bodyY(){

        return this.floorY-15;
    }

    update(dt,opponent){

        if(this.dead)
            return;

        this.anim+=dt;

        this.attackCooldown=
            Math.max(
                0,
                this.attackCooldown-dt
            );

        this.skillCooldown=
            Math.max(
                0,
                this.skillCooldown-dt
            );

        this.dashCooldown=
            Math.max(
                0,
                this.dashCooldown-dt
            );

        this.heavyCooldown=
            Math.max(
                0,
                this.heavyCooldown-dt
            );

        this.ultimateCooldown=
            Math.max(
                0,
                this.ultimateCooldown-dt
            );

        this.dashInvincible=
            Math.max(
                0,
                this.dashInvincible-dt
            );

        this.hitFlash=
            Math.max(
                0,
                this.hitFlash-dt
            );

        this.hitStun=
            Math.max(
                0,
                this.hitStun-dt
            );

        this.comboTimer=
            Math.max(
                0,
                this.comboTimer-dt
            );

        if(this.comboTimer<=0){
            this.combo=0;
        }

        this.energy=
            clamp(
                this.energy+
                8*dt,
                0,
                100
            );

        if(this.hitStun>0){

            this.vx*=.92;

            this.vy+=
                1450*dt;

            this.y+=
                this.vy*dt;

            if(this.y>=0){

                this.y=0;
                this.vy=0;
                this.grounded=true;
            }

            return;
        }

        if(this.dashTimer>0){

            this.dashTimer-=dt;

            this.x+=
                this.vx*dt;

            if(
                Math.random()<.82
            ){

                makeAfterimage(
                    this
                );
            }

            this.y=0;

        }else{

            this.control(
                dt,
                opponent
            );

            this.vy+=
                1450*dt;

            this.y+=
                this.vy*dt;

            if(this.y>=0){

                this.y=0;
                this.vy=0;
                this.grounded=true;

            }else{

                this.grounded=false;
            }

            this.x+=
                this.vx*dt;

            if(this.grounded){

                this.vx*=
                    Math.pow(.0008,dt);

            }else{

                this.vx*=
                    Math.pow(.08,dt);
            }
        }

        this.x=
            clamp(
                this.x,
                65,
                W-65
            );

        if(this.attackTimer>0){
            this.attackTimer-=dt;
        }

        if(
            this.x>
            opponent.x+4
        ){

            this.facing=-1;

        }else if(
            this.x<
            opponent.x-4
        ){

            this.facing=1;
        }
    }

    control(dt,opponent){

        if(this.side===1){

            let move=0;

            if(keys["a"])
                move-=1;

            if(keys["d"])
                move+=1;

            if(move!==0){

                this.vx+=
                    move*1500*dt;

                this.vx=
                    clamp(
                        this.vx,
                        -285,
                        285
                    );

                this.state="run";

            }else{

                this.state=
                    this.grounded
                    ?"idle"
                    :"jump";
            }

            if(
                keys["w"]&&
                this.grounded
            ){

                this.vy=-580;

                this.grounded=false;

                particle(
                    this.x,
                    this.bodyY+50,
                    this.data.color,
                    14,
                    90
                );

                sfxJump();
            }

            if(
                keys["s"]&&
                !this.grounded
            ){

                this.vy+=
                    1100*dt;
            }

            if(keys["j"]){

                this.normalAttack();

                keys["j"]=false;
            }

            if(keys["k"]){

                this.skill();

                keys["k"]=false;
            }

            if(keys["l"]){

                this.dash();

                keys["l"]=false;
            }

            if(keys["u"]){

                this.heavy();

                keys["u"]=false;
            }

            if(keys["i"]){

                this.ultimate(
                    opponent
                );

                keys["i"]=false;
            }

        }else{

            if(gameMode==="cpu"){

                this.cpuControl(
                    dt,
                    opponent
                );

            }else{

                let move=0;

                if(keys["arrowleft"])
                    move-=1;

                if(keys["arrowright"])
                    move+=1;

                if(move!==0){

                    this.vx+=
                        move*1500*dt;

                    this.vx=
                        clamp(
                            this.vx,
                            -285,
                            285
                        );

                    this.state="run";

                }else{

                    this.state=
                        this.grounded
                        ?"idle"
                        :"jump";
                }

                if(
                    keys["arrowup"]&&
                    this.grounded
                ){

                    this.vy=-580;

                    this.grounded=false;

                    particle(
                        this.x,
                        this.bodyY+50,
                        this.data.color,
                        14,
                        90
                    );

                    sfxJump();
                }

                if(
                    keys["arrowdown"]&&
                    !this.grounded
                ){

                    this.vy+=
                        1100*dt;
                }

                if(keys["1"]){

                    this.normalAttack();

                    keys["1"]=false;
                }

                if(keys["2"]){

                    this.skill();

                    keys["2"]=false;
                }

                if(keys["3"]){

                    this.dash();

                    keys["3"]=false;
                }

                if(keys["4"]){

                    this.heavy();

                    keys["4"]=false;
                }

                if(keys["5"]){

                    this.ultimate(
                        opponent
                    );

                    keys["5"]=false;
                }
            }
        }
    }

    /* =====================================================
       HARD CPU
    ===================================================== */

    cpuControl(dt,opponent){

        const dx=
            opponent.x-this.x;

        const ad=
            Math.abs(dx);

        const direction=
            Math.sign(dx)||1;

        this.cpuThink-=dt;

        this.cpuAttackDelay-=dt;
        this.cpuDashDelay-=dt;
        this.cpuSkillDelay-=dt;
        this.cpuHeavyDelay-=dt;
        this.cpuUltDelay-=dt;

        /*
           CPU mới:
           - áp sát thông minh
           - biết lùi khi gần
           - biết giữ khoảng cách
           - dash khi player chuẩn bị đánh
           - skill từ xa
           - heavy khi áp sát
           - ultimate rất chủ động
        */

        if(this.cpuThink<=0){

            this.cpuThink=
                rand(.035,.09);

            if(ad>500){

                this.cpuMove=
                    direction;

            }else if(ad>300){

                this.cpuMove=
                    Math.random()<.82
                    ?direction
                    :0;

            }else if(ad>180){

                this.cpuMove=
                    Math.random()<.65
                    ?direction
                    :-direction;

            }else if(ad>105){

                this.cpuMove=
                    Math.random()<.72
                    ?direction
                    :-direction;

            }else{

                /*
                   Ở quá gần:
                   CPU có lúc lùi,
                   có lúc giữ vị trí
                   để combo.
                */

                const r=Math.random();

                if(r<.45){

                    this.cpuMove=
                        -direction;

                }else{

                    this.cpuMove=0;
                }
            }

            /*
               CPU nhảy né thường xuyên hơn
            */

            if(
                this.grounded&&
                Math.random()<.13
            ){

                this.cpuJump=true;
            }
        }

        if(this.cpuMove!==0){

            this.vx+=
                this.cpuMove*
                1550*
                dt;

            this.vx=
                clamp(
                    this.vx,
                    -310,
                    310
                );

            this.state="run";

        }else{

            this.state=
                this.grounded
                ?"idle"
                :"jump";
        }

        /*
           Né bằng nhảy
        */

        if(
            this.cpuJump&&
            this.grounded
        ){

            this.vy=-600;

            this.grounded=false;

            this.cpuJump=false;

            sfxJump();
        }

        /*
           Tấn công thường:
           CPU có thể combo.
        */

        if(
            ad<145&&
            this.cpuAttackDelay<=0
        ){

            this.cpuAttackDelay=
                rand(.08,.22);

            this.normalAttack();
        }

        /*
           Heavy khi đủ gần.
        */

        if(
            ad<175&&
            this.heavyCooldown<=0&&
            this.cpuHeavyDelay<=0
        ){

            this.cpuHeavyDelay=
                rand(.3,.65);

            this.heavy();
        }

        /*
           Skill:
           CPU ưu tiên dùng khi
           khoảng cách 150-430.
        */

        if(
            ad>150&&
            ad<450&&
            this.energy>=25&&
            this.skillCooldown<=0&&
            this.cpuSkillDelay<=0
        ){

            this.cpuSkillDelay=
                rand(.35,.75);

            this.skill();
        }

        /*
           Dash:
           vừa dùng để áp sát,
           vừa né khi quá gần.
        */

        if(
            this.dashCooldown<=0&&
            this.cpuDashDelay<=0
        ){

            const shouldDash=
                (
                    ad>190&&
                    ad<500
                )||
                (
                    ad<120&&
                    Math.random()<.65
                );

            if(
                shouldDash&&
                Math.random()<.30
            ){

                this.cpuDashDelay=
                    rand(.5,1.1);

                /*
                   nếu gần thì đôi khi
                   dash xuyên qua đối thủ
                */

                if(ad<150){

                    this.facing=
                        -direction;
                }else{

                    this.facing=
                        direction;
                }

                this.dash();
            }
        }

        /*
           Ultimate:
           CPU rất nguy hiểm khi
           player đang trong tầm.
        */

        if(
            this.energy>=100&&
            this.ultimateCooldown<=0
        ){

            if(
                ad<360&&
                Math.random()<.35
            ){

                this.ultimate(
                    opponent
                );

            }else if(
                opponent.hp<38&&
                ad<500&&
                Math.random()<.16
            ){

                this.ultimate(
                    opponent
                );
            }
        }

        /*
           CPU cố gắng né khi
           đối phương đang attack.
        */

        if(
            opponent.attackTimer>0&&
            ad<150&&
            this.dashCooldown<=0&&
            Math.random()<.42
        ){

            this.facing=
                Math.random()<.5
                ?-direction
                :direction;

            this.dash();
        }
    }

    /* =====================================================
       ATTACK
    ===================================================== */

    normalAttack(){

        if(
            this.attackCooldown>0
        )
            return;

        this.attackCooldown=.28;
        this.attackTimer=.18;

        this.state="attack";

        this.combo++;

        if(this.combo>3){
            this.combo=1;
        }

        this.comboTimer=.68;

        const reach=
            this.combo===3
            ?125
            :108;

        const targetX=
            this.x+
            this.facing*
            reach;

        slash(
            this.x,
            this.bodyY-5,
            this.data.color,
            this.facing,
            this.combo===3
            ?62
            :45,
            this.combo===3
            ?.28
            :.22
        );

        particle(
            this.x+
            this.facing*65,
            this.bodyY-10,
            this.data.color,
            this.combo===3
            ?18
            :10,
            this.combo===3
            ?170
            :100
        );

        if(
            Math.abs(
                targetX-
                enemy.x
            )<82&&
            Math.abs(
                this.bodyY-
                enemy.bodyY
            )<90
        ){

            let damage=7;

            if(this.combo===2)
                damage=8;

            if(this.combo===3)
                damage=11;

            enemy.takeDamage(
                damage,
                this.facing
            );

            this.energy=
                clamp(
                    this.energy+7,
                    0,
                    100
                );
        }

        sfxSlash();
    }

    /* =====================================================
       SKILL
    ===================================================== */

    skill(){

        if(
            this.skillCooldown>0||
            this.energy<25
        )
            return;

        this.energy-=25;

        this.skillCooldown=.85;

        this.attackTimer=.3;

        this.state="skill";

        projectiles.push({

            owner:this,

            x:
                this.x+
                this.facing*55,

            y:
                this.bodyY-35,

            vx:
                this.facing*
                this.getProjectileSpeed(),

            life:1.55,

            damage:
                this.getSkillDamage(),

            type:
                this.data.projectile,

            size:
                this.data.style==="wind"
                ?32
                :23,

            rot:0
        });

        /*
           riêng từng hệ
        */

        if(
            this.data.style===
            "water"
        ){

            for(
                let i=0;
                i<4;
                i++
            ){

                waterArcs.push({

                    x:this.x+
                        this.facing*35,

                    y:this.bodyY-
                        25,

                    life:.7,

                    rot:
                        i*.8
                });
            }

        }else if(
            this.data.style===
            "fire"
        ){

            for(
                let i=0;
                i<9;
                i++
            ){

                fireTrails.push({

                    x:this.x+
                        this.facing*
                        rand(20,75),

                    y:this.bodyY+
                        rand(-50,25),

                    vx:
                        this.facing*
                        rand(80,220),

                    life:
                        .45+
                        Math.random()*.25
                });
            }

        }else if(
            this.data.style===
            "thunder"
        ){

            for(
                let i=0;
                i<3;
                i++
            ){

                lightningBolts.push({

                    x:
                        this.x+
                        this.facing*
                        rand(20,90),

                    y:
                        this.bodyY+
                        rand(-80,20),

                    life:.3
                });
            }

        }else if(
            this.data.style===
            "rock"
        ){

            for(
                let i=0;
                i<9;
                i++
            ){

                rockChunks.push({

                    x:this.x+
                        this.facing*
                        rand(20,75),

                    y:this.bodyY+
                        rand(-50,30),

                    vx:
                        this.facing*
                        rand(50,180),

                    vy:
                        rand(-160,-40),

                    life:
                        .6+
                        Math.random()*.4
                });
            }
        }

        particle(
            this.x+
            this.facing*40,
            this.bodyY-35,
            this.data.color,
            22,
            150
        );

        ring(
            this.x+
            this.facing*40,
            this.bodyY-35,
            this.data.color,
            55
        );

        sfxSkill(
            this.data.style
        );
    }

    getProjectileSpeed(){

        if(
            this.data.style===
            "thunder"
        )
            return 900;

        if(
            this.data.style===
            "wind"
        )
            return 820;

        if(
            this.data.style===
            "fire"
        )
            return 680;

        if(
            this.data.style===
            "water"
        )
            return 640;

        return 590;
    }

    getSkillDamage(){

        if(
            this.data.style===
            "rock"
        )
            return 19;

        if(
            this.data.style===
            "thunder"
        )
            return 18;

        if(
            this.data.style===
            "wind"
        )
            return 17;

        if(
            this.data.style===
            "fire"
        )
            return 16;

        return 15;
    }

    /* =====================================================
       DASH
    ===================================================== */

    dash(){

        if(
            this.dashCooldown>0
        )
            return;

        this.dashCooldown=.62;

        this.dashTimer=.19;

        this.dashInvincible=.19;

        this.vx=
            this.facing*
            1250;

        this.state="dash";

        for(
            let i=0;
            i<7;
            i++
        ){

            makeAfterimage(this);
        }

        particle(
            this.x-
            this.facing*25,
            this.bodyY,
            this.data.color,
            24,
            200
        );

        ring(
            this.x,
            this.bodyY,
            this.data.color,
            55
        );

        if(
            this.data.style===
            "wind"
        ){

            for(
                let i=0;
                i<10;
                i++
            ){

                windBlades.push({

                    x:
                        this.x-
                        this.facing*
                        rand(0,120),

                    y:
                        this.bodyY+
                        rand(-55,40),

                    vx:
                        this.facing*
                        rand(100,300),

                    life:.55,

                    size:
                        rand(20,50),

                    rot:
                        rand(-.5,.5)
                });
            }
        }

        sfxDash(
            this.data.style
        );
    }

    /* =====================================================
       HEAVY
    ===================================================== */

    heavy(){

        if(
            this.heavyCooldown>0
        )
            return;

        this.heavyCooldown=.65;

        this.attackTimer=.32;

        this.state="heavy";

        const reach=145;

        const targetX=
            this.x+
            this.facing*
            reach;

        slash(
            this.x,
            this.bodyY-5,
            this.data.color,
            this.facing,
            90,
            .38
        );

        ring(
            this.x+
            this.facing*75,
            this.bodyY,
            this.data.color,
            70
        );

        particle(
            this.x+
            this.facing*80,
            this.bodyY,
            this.data.color,
            28,
            210
        );

        if(
            Math.abs(
                targetX-
                enemy.x
            )<100&&
            Math.abs(
                this.bodyY-
                enemy.bodyY
            )<105
        ){

            enemy.takeDamage(
                13,
                this.facing
            );

            this.energy=
                clamp(
                    this.energy+10,
                    0,
                    100
                );
        }

        sfxHeavy();
    }

    /* =====================================================
       ULTIMATE
    ===================================================== */

    ultimate(opponent){

        if(
            this.energy<100||
            this.ultimateCooldown>0
        )
            return;

        this.energy=0;

        this.ultimateCooldown=4;

        this.attackTimer=.8;

        this.state="ultimate";

        const distance=
            Math.abs(
                this.x-
                opponent.x
            );

        ultimateEffect(this);

        if(
            distance<330
        ){

            opponent.takeDamage(
                32,
                this.facing
            );

            opponent.vx=
                this.facing*
                440;

            opponent.vy=-280;
        }

        sfxUltimate(
            this.data.style
        );
    }

    /* =====================================================
       DAMAGE
    ===================================================== */

    takeDamage(
        damage,
        dir
    ){

        if(
            this.dashInvincible>0
        )
            return;

        if(this.dead)
            return;

        this.hp-=damage;

        this.hitFlash=.18;

        this.hitStun=.12;

        this.vx=
            dir*
            300;

        this.vy=-180;

        this.state="hit";

        particle(
            this.x,
            this.bodyY-30,
            "#ffffff",
            16,
            200
        );

        ring(
            this.x,
            this.bodyY-25,
            "#ffffff",
            38
        );

        sfxHit();

        if(this.hp<=0){

            this.hp=0;

            this.dead=true;

            particle(
                this.x,
                this.bodyY-30,
                this.data.color,
                65,
                350
            );

            ring(
                this.x,
                this.bodyY-30,
                this.data.color,
                110
            );
        }
    }

    /* =====================================================
       DRAW
    ===================================================== */

    draw(){

        const x=this.x;

        const y=
            this.bodyY+
            this.y;

        const bob=
            this.state==="idle"
            ?Math.sin(
                this.anim*4
            )*2
            :0;

        const yy=
            y+bob;

        ctx.save();

        if(
            this.hitFlash>0
        ){
            ctx.globalAlpha=.78;
        }

        drawCharacterAura(
            this,
            x,
            yy
        );

        drawCharacterShadow(
            this,
            x,
            yy
        );

        drawCharacterBody(
            this,
            x,
            yy
        );

        drawCharacterWeapon(
            this,
            x,
            yy
        );

        if(
            this.state==="attack"||
            this.state==="heavy"
        ){

            drawAttackPose(
                this,
                x,
                yy
            );
        }

        if(
            this.state==="skill"
        ){

            drawSkillPose(
                this,
                x,
                yy
            );
        }

        if(
            this.state==="ultimate"
        ){

            drawUltimatePose(
                this,
                x,
                yy
            );
        }

        ctx.restore();
    }
}

/* =========================================================
   CHARACTER AURA
========================================================= */

function drawCharacterAura(
    f,
    x,
    y
){

    const c=f.data.color;

    const pulse=
        1+
        Math.sin(
            f.anim*6
        )*.08;

    /*
       KAZE:
       nhiều lớp gió
    */

    if(
        f.data.style===
        "wind"
    ){

        ctx.save();

        ctx.globalAlpha=.15;

        for(
            let i=0;
            i<7;
            i++
        ){

            ctx.beginPath();

            ctx.ellipse(
                x+
                    Math.sin(
                        f.anim*2+
                        i
                    )*5,

                y-45,

                (
                    48+
                    i*15
                )*pulse,

                (
                    78+
                    i*16
                )*pulse,

                Math.sin(
                    f.anim*1.4+i
                )*.4,

                0,
                Math.PI*2
            );

            ctx.strokeStyle=c;

            ctx.lineWidth=
                i%2===0
                ?4
                :2;

            ctx.shadowBlur=20;
            ctx.shadowColor=c;

            ctx.stroke();
        }

        ctx.restore();

        return;
    }

    /*
       Fire
    */

    if(
        f.data.style===
        "fire"
    ){

        ctx.save();

        ctx.globalAlpha=.18;

        for(
            let i=0;
            i<7;
            i++
        ){

            const a=
                Math.sin(
                    f.anim*5+
                    i
                )*10;

            ctx.fillStyle=
                i%2===0
                ?"#ff5a36"
                :"#ffb329";

            ctx.beginPath();

            ctx.moveTo(
                x-65+i*20,
                y+20
            );

            ctx.quadraticCurveTo(
                x-50+i*20+a,
                y-80-i*3,
                x-40+i*20,
                y-135
            );

            ctx.quadraticCurveTo(
                x-20+i*20,
                y-75,
                x-10+i*20,
                y+20
            );

            ctx.fill();
        }

        ctx.restore();

    }else if(
        f.data.style===
        "water"
    ){

        ctx.save();

        ctx.globalAlpha=.20;

        ctx.strokeStyle=c;
        ctx.lineWidth=4;

        for(
            let i=0;
            i<5;
            i++
        ){

            ctx.beginPath();

            ctx.arc(
                x,
                y-30,
                55+i*14,
                Math.sin(
                    f.anim*2+i
                ),
                Math.sin(
                    f.anim*2+i
                )+2.8
            );

            ctx.stroke();
        }

        ctx.restore();

    }else if(
        f.data.style===
        "thunder"
    ){

        ctx.save();

        ctx.globalAlpha=.55;

        ctx.strokeStyle="#fff58b";
        ctx.shadowBlur=20;
        ctx.shadowColor=c;

        for(
            let i=0;
            i<5;
            i++
        ){

            ctx.beginPath();

            ctx.moveTo(
                x+
                    rand(-55,55),
                y-105
            );

            ctx.lineTo(
                x+
                    rand(-40,40),
                y-55
            );

            ctx.lineTo(
                x+
                    rand(-65,65),
                y
            );

            ctx.stroke();
        }

        ctx.restore();

    }else if(
        f.data.style===
        "flower"
    ){

        ctx.save();

        ctx.globalAlpha=.55;

        for(
            let i=0;
            i<10;
            i++
        ){

            const a=
                f.anim*.8+
                i*.62;

            const r=
                55+
                (i%3)*20;

            ctx.fillStyle=
                i%2===0
                ?"#ff79c8"
                :"#ffb4e4";

            ctx.beginPath();

            ctx.ellipse(
                x+
                    Math.cos(a)*r,
                y-45+
                    Math.sin(a)*r*.7,
                5,
                11,
                a,
                0,
                Math.PI*2
            );

            ctx.fill();
        }

        ctx.restore();

    }else if(
        f.data.style===
        "rock"
    ){

        ctx.save();

        ctx.globalAlpha=.30;

        ctx.fillStyle="#9f9277";

        for(
            let i=0;
            i<9;
            i++
        ){

            const a=
                i*Math.PI*2/9;

            const r=
                55+
                Math.sin(
                    f.anim*2+i
                )*7;

            ctx.beginPath();

            ctx.moveTo(
                x+
                    Math.cos(a)*r,
                y-45+
                    Math.sin(a)*r
            );

            ctx.lineTo(
                x+
                    Math.cos(a+.3)*
                    (r+20),
                y-45+
                    Math.sin(a+.3)*
                    (r+20)
            );

            ctx.lineTo(
                x+
                    Math.cos(a-.2)*
                    (r+14),
                y-45+
                    Math.sin(a-.2)*
                    (r+14)
            );

            ctx.closePath();

            ctx.fill();
        }

        ctx.restore();
    }

    /*
       Aura chung
    */

    ctx.save();

    const g=
        ctx.createRadialGradient(
            x,
            y-50,
            5,
            x,
            y-50,
            115
        );

    g.addColorStop(
        0,
        c+"55"
    );

    g.addColorStop(
        .45,
        c+"18"
    );

    g.addColorStop(
        1,
        "transparent"
    );

    ctx.fillStyle=g;

    ctx.beginPath();

    ctx.arc(
        x,
        y-45,
        110*pulse,
        0,
        Math.PI*2
    );

    ctx.fill();

    ctx.restore();
}

/* =========================================================
   SHADOW
========================================================= */

function drawCharacterShadow(
    f,
    x,
    y
){

    ctx.save();

    ctx.globalAlpha=.35;

    ctx.fillStyle="#000";

    ctx.beginPath();

    ctx.ellipse(
        x,
        f.floorY+5,
        48,
        11,
        0,
        0,
        Math.PI*2
    );

    ctx.fill();

    ctx.restore();
}

/* =========================================================
   BODY
========================================================= */

function drawCharacterBody(
    f,
    x,
    y
){

    const c=f.data.color;
    const dark=f.data.dark;
    const light=f.data.light;

    const moving=
        f.state==="run";

    const walk=
        moving
        ?Math.sin(
            f.anim*13
        )*9
        :0;

    ctx.save();

    ctx.translate(
        x,
        y
    );

    ctx.scale(
        f.facing,
        1
    );

    /* legs */

    ctx.strokeStyle="#171827";

    ctx.lineWidth=14;

    ctx.lineCap="round";

    ctx.beginPath();

    ctx.moveTo(
        -12,
        43
    );

    ctx.lineTo(
        -15+walk,
        76
    );

    ctx.stroke();

    ctx.beginPath();

    ctx.moveTo(
        12,
        43
    );

    ctx.lineTo(
        15-walk,
        76
    );

    ctx.stroke();

    /* boots */

    ctx.fillStyle="#090b16";

    ctx.beginPath();

    ctx.roundRect(
        -28+walk,
        69,
        27,
        11,
        5
    );

    ctx.fill();

    ctx.beginPath();

    ctx.roundRect(
        2-walk,
        69,
        27,
        11,
        5
    );

    ctx.fill();

    /* uniform */

    ctx.fillStyle="#151829";

    ctx.beginPath();

    ctx.moveTo(
        -27,
        -3
    );

    ctx.lineTo(
        27,
        -3
    );

    ctx.lineTo(
        24,
        48
    );

    ctx.lineTo(
        0,
        57
    );

    ctx.lineTo(
        -24,
        48
    );

    ctx.closePath();

    ctx.fill();

    /* elemental coat */

    if(
        f.data.style===
        "water"
    ){

        ctx.fillStyle="#155d91";

        ctx.beginPath();

        ctx.moveTo(
            -33,
            -8
        );

        ctx.lineTo(
            -5,
            -2
        );

        ctx.lineTo(
            -13,
            54
        );

        ctx.lineTo(
            -39,
            42
        );

        ctx.closePath();

        ctx.fill();

        ctx.fillStyle="#1b85ba";

        ctx.beginPath();

        ctx.moveTo(
            33,
            -8
        );

        ctx.lineTo(
            5,
            -2
        );

        ctx.lineTo(
            13,
            54
        );

        ctx.lineTo(
            39,
            42
        );

        ctx.closePath();

        ctx.fill();

        drawWaterPattern(
            -30,
            10,
            c
        );

        drawWaterPattern(
            30,
            10,
            c
        );

    }else if(
        f.data.style===
        "fire"
    ){

        ctx.fillStyle="#7e211d";

        ctx.beginPath();

        ctx.moveTo(
            -35,
            -9
        );

        ctx.lineTo(
            -4,
            -2
        );

        ctx.lineTo(
            -13,
            56
        );

        ctx.lineTo(
            -41,
            42
        );

        ctx.closePath();

        ctx.fill();

        ctx.fillStyle="#a93420";

        ctx.beginPath();

        ctx.moveTo(
            35,
            -9
        );

        ctx.lineTo(
            4,
            -2
        );

        ctx.lineTo(
            13,
            56
        );

        ctx.lineTo(
            41,
            42
        );

        ctx.closePath();

        ctx.fill();

        drawFlamePattern(
            -29,
            16
        );

        drawFlamePattern(
            29,
            16
        );

    }else if(
        f.data.style===
        "thunder"
    ){

        ctx.fillStyle="#493d72";

        ctx.beginPath();

        ctx.moveTo(
            -35,
            -8
        );

        ctx.lineTo(
            -4,
            -2
        );

        ctx.lineTo(
            -14,
            55
        );

        ctx.lineTo(
            -41,
            41
        );

        ctx.closePath();

        ctx.fill();

        ctx.fillStyle="#65528f";

        ctx.beginPath();

        ctx.moveTo(
            35,
            -8
        );

        ctx.lineTo(
            4,
            -2
        );

        ctx.lineTo(
            14,
            55
        );

        ctx.lineTo(
            41,
            41
        );

        ctx.closePath();

        ctx.fill();

        drawLightningPattern(
            -28,
            18
        );

        drawLightningPattern(
            28,
            18
        );

    }else if(
        f.data.style===
        "flower"
    ){

        ctx.fillStyle="#7b315f";

        ctx.beginPath();

        ctx.moveTo(
            -35,
            -8
        );

        ctx.lineTo(
            -4,
            -2
        );

        ctx.lineTo(
            -13,
            56
        );

        ctx.lineTo(
            -42,
            40
        );

        ctx.closePath();

        ctx.fill();

        ctx.fillStyle="#a94b82";

        ctx.beginPath();

        ctx.moveTo(
            35,
            -8
        );

        ctx.lineTo(
            4,
            -2
        );

        ctx.lineTo(
            13,
            56
        );

        ctx.lineTo(
            42,
            40
        );

        ctx.closePath();

        ctx.fill();

        drawFlowerPattern(
            -28,
            17
        );

        drawFlowerPattern(
            28,
            17
        );

    }else if(
        f.data.style===
        "rock"
    ){

        ctx.fillStyle="#4e483f";

        ctx.beginPath();

        ctx.moveTo(
            -35,
            -8
        );

        ctx.lineTo(
            -4,
            -2
        );

        ctx.lineTo(
            -13,
            56
        );

        ctx.lineTo(
            -42,
            40
        );

        ctx.closePath();

        ctx.fill();

        ctx.fillStyle="#706556";

        ctx.beginPath();

        ctx.moveTo(
            35,
            -8
        );

        ctx.lineTo(
            4,
            -2
        );

        ctx.lineTo(
            14,
            55
        );

        ctx.lineTo(
            42,
            40
        );

        ctx.closePath();

        ctx.fill();

        drawRockPattern(
            -28,
            18
        );

        drawRockPattern(
            28,
            18
        );

    }else if(
        f.data.style===
        "wind"
    ){

        ctx.fillStyle="#174f4b";

        ctx.beginPath();

        ctx.moveTo(
            -36,
            -10
        );

        ctx.lineTo(
            -4,
            -2
        );

        ctx.lineTo(
            -17,
            57
        );

        ctx.lineTo(
            -45,
            38
        );

        ctx.closePath();

        ctx.fill();

        ctx.fillStyle="#216d65";

        ctx.beginPath();

        ctx.moveTo(
            36,
            -10
        );

        ctx.lineTo(
            4,
            -2
        );

        ctx.lineTo(
            17,
            57
        );

        ctx.lineTo(
            45,
            38
        );

        ctx.closePath();

        ctx.fill();

        drawWindPattern(
            -29,
            17
        );

        drawWindPattern(
            29,
            17
        );

        /*
           dải vải bay
        */

        ctx.strokeStyle="#8fffe9";

        ctx.globalAlpha=.70;

        ctx.lineWidth=3;

        ctx.beginPath();

        ctx.moveTo(
            32,
            4
        );

        ctx.bezierCurveTo(
            65,
            -12,
            75,
            16,
            105,
            2
        );

        ctx.stroke();

        ctx.beginPath();

        ctx.moveTo(
            -32,
            14
        );

        ctx.bezierCurveTo(
            -60,
            2,
            -74,
            30,
            -98,
            13
        );

        ctx.stroke();

        ctx.globalAlpha=1;
    }

    /* belt */

    ctx.fillStyle=dark;

    ctx.fillRect(
        -27,
        35,
        54,
        7
    );

    ctx.fillStyle=light;

    ctx.beginPath();

    ctx.arc(
        0,
        39,
        5,
        0,
        Math.PI*2
    );

    ctx.fill();

    /* neck */

    ctx.fillStyle="#d39b7e";

    ctx.fillRect(
        -7,
        -18,
        14,
        15
    );

    /* head */

    ctx.fillStyle="#dca785";

    ctx.beginPath();

    ctx.arc(
        0,
        -43,
        25,
        0,
        Math.PI*2
    );

    ctx.fill();

    drawHair(f);
    drawEyes(f);

    /* nose */

    ctx.strokeStyle="#9a6358";
    ctx.lineWidth=1;

    ctx.beginPath();

    ctx.moveTo(
        5,
        -39
    );

    ctx.lineTo(
        7,
        -36
    );

    ctx.stroke();

    /* mouth */

    ctx.strokeStyle="#783f49";

    ctx.beginPath();

    ctx.moveTo(
        3,
        -28
    );

    ctx.lineTo(
        10,
        -28
    );

    ctx.stroke();

    /* arms */

    const armSwing=
        moving
        ?Math.sin(
            f.anim*13
        )*12
        :0;

    ctx.strokeStyle="#161824";

    ctx.lineWidth=12;

    ctx.beginPath();

    ctx.moveTo(
        -24,
        0
    );

    ctx.lineTo(
        -38,
        -5+
        armSwing
    );

    ctx.stroke();

    ctx.beginPath();

    ctx.moveTo(
        24,
        0
    );

    ctx.lineTo(
        38,
        -5-
        armSwing
    );

    ctx.stroke();

    ctx.strokeStyle=c;

    ctx.lineWidth=8;

    ctx.beginPath();

    ctx.moveTo(
        -24,
        0
    );

    ctx.lineTo(
        -39,
        -5+
        armSwing
    );

    ctx.stroke();

    ctx.beginPath();

    ctx.moveTo(
        24,
        0
    );

    ctx.lineTo(
        39,
        -5-
        armSwing
    );

    ctx.stroke();

    ctx.restore();
}

/* =========================================================
   HAIR
========================================================= */

function drawHair(f){

    let hair="#151728";

    if(
        f.data.style===
        "wind"
    )
        hair="#163a3a";

    if(
        f.data.style===
        "thunder"
    )
        hair="#22243b";

    if(
        f.data.style===
        "flower"
    )
        hair="#241728";

    if(
        f.data.style===
        "fire"
    )
        hair="#241313";

    if(
        f.data.style===
        "water"
    )
        hair="#102433";

    if(
        f.data.style===
        "rock"
    )
        hair="#25231f";

    ctx.fillStyle=hair;

    ctx.beginPath();

    ctx.moveTo(
        -25,
        -51
    );

    ctx.quadraticCurveTo(
        -20,
        -78,
        -2,
        -72
    );

    ctx.quadraticCurveTo(
        12,
        -84,
        25,
        -55
    );

    ctx.lineTo(
        20,
        -35
    );

    ctx.lineTo(
        12,
        -48
    );

    ctx.lineTo(
        6,
        -30
    );

    ctx.lineTo(
        0,
        -47
    );

    ctx.lineTo(
        -9,
        -31
    );

    ctx.lineTo(
        -12,
        -49
    );

    ctx.lineTo(
        -23,
        -35
    );

    ctx.closePath();

    ctx.fill();

    ctx.strokeStyle=
        f.data.color;

    ctx.lineWidth=3;

    ctx.globalAlpha=.65;

    ctx.beginPath();

    ctx.moveTo(
        -15,
        -60
    );

    ctx.quadraticCurveTo(
        -6,
        -72,
        4,
        -63
    );

    ctx.stroke();

    ctx.beginPath();

    ctx.moveTo(
        4,
        -63
    );

    ctx.quadraticCurveTo(
        13,
        -70,
        19,
        -55
    );

    ctx.stroke();

    ctx.globalAlpha=1;
}

/* =========================================================
   EYES
========================================================= */

function drawEyes(f){

    ctx.fillStyle="#121322";

    ctx.beginPath();

    ctx.ellipse(
        -9,
        -42,
        6,
        4,
        0,
        0,
        Math.PI*2
    );

    ctx.fill();

    ctx.beginPath();

    ctx.ellipse(
        9,
        -42,
        6,
        4,
        0,
        0,
        Math.PI*2
    );

    ctx.fill();

    ctx.fillStyle=
        f.data.light;

    ctx.beginPath();

    ctx.arc(
        -8,
        -43,
        2,
        0,
        Math.PI*2
    );

    ctx.fill();

    ctx.beginPath();

    ctx.arc(
        10,
        -43,
        2,
        0,
        Math.PI*2
    );

    ctx.fill();
}

/* =========================================================
   PATTERNS
========================================================= */

function drawWaterPattern(
    x,
    y,
    c
){

    ctx.strokeStyle=c;
    ctx.lineWidth=2;

    ctx.beginPath();

    ctx.arc(
        x,
        y,
        9,
        0,
        Math.PI
    );

    ctx.stroke();

    ctx.beginPath();

    ctx.arc(
        x+4,
        y+8,
        7,
        Math.PI,
        Math.PI*2
    );

    ctx.stroke();
}

function drawFlamePattern(
    x,
    y
){

    ctx.fillStyle="#ffb126";

    ctx.beginPath();

    ctx.moveTo(
        x,
        y+12
    );

    ctx.quadraticCurveTo(
        x-8,
        y,
        x,
        y-7
    );

    ctx.quadraticCurveTo(
        x+8,
        y,
        x+2,
        y+12
    );

    ctx.fill();
}

function drawLightningPattern(
    x,
    y
){

    ctx.strokeStyle="#ffe96b";
    ctx.lineWidth=2;

    ctx.beginPath();

    ctx.moveTo(
        x-4,
        y-9
    );

    ctx.lineTo(
        x+3,
        y
    );

    ctx.lineTo(
        x-3,
        y+2
    );

    ctx.lineTo(
        x+5,
        y+11
    );

    ctx.stroke();
}

function drawFlowerPattern(
    x,
    y
){

    ctx.fillStyle="#ffb5e5";

    for(
        let i=0;
        i<5;
        i++
    ){

        const a=
            i*
            Math.PI*
            2/
            5;

        ctx.beginPath();

        ctx.ellipse(
            x+
                Math.cos(a)*6,
            y+
                Math.sin(a)*6,
            4,
            7,
            a,
            0,
            Math.PI*2
        );

        ctx.fill();
    }
}

function drawRockPattern(
    x,
    y
){

    ctx.strokeStyle="#b8aa8d";

    ctx.lineWidth=2;

    ctx.beginPath();

    ctx.moveTo(
        x-9,
        y-5
    );

    ctx.lineTo(
        x-2,
        y-10
    );

    ctx.lineTo(
        x+8,
        y-3
    );

    ctx.lineTo(
        x+3,
        y+8
    );

    ctx.lineTo(
        x-8,
        y+5
    );

    ctx.closePath();

    ctx.stroke();
}

function drawWindPattern(
    x,
    y
){

    ctx.strokeStyle="#9affea";

    ctx.lineWidth=2;

    ctx.beginPath();

    ctx.arc(
        x,
        y,
        10,
        -.7,
        1.5
    );

    ctx.stroke();

    ctx.beginPath();

    ctx.arc(
        x+3,
        y+5,
        7,
        -.8,
        1.4
    );

    ctx.stroke();
}

/* =========================================================
   WEAPON
========================================================= */

function drawCharacterWeapon(
    f,
    x,
    y
){

    ctx.save();

    ctx.translate(
        x,
        y
    );

    ctx.scale(
        f.facing,
        1
    );

    let bladeColor="#dfeeff";

    if(
        f.data.style===
        "wind"
    )
        bladeColor="#b9fff2";

    if(
        f.data.style===
        "fire"
    )
        bladeColor="#fff1cf";

    if(
        f.data.style===
        "thunder"
    )
        bladeColor="#fffbd0";

    if(
        f.data.style===
        "flower"
    )
        bladeColor="#ffe0f4";

    if(
        f.data.style===
        "rock"
    )
        bladeColor="#d7d1c0";

    ctx.strokeStyle="#6e472f";
    ctx.lineWidth=5;

    ctx.beginPath();

    ctx.moveTo(
        37,
        -8
    );

    ctx.lineTo(
        63,
        -30
    );

    ctx.stroke();

    ctx.strokeStyle=
        bladeColor;

    ctx.lineWidth=4;

    ctx.shadowBlur=9;
    ctx.shadowColor=
        f.data.color;

    ctx.beginPath();

    ctx.moveTo(
        62,
        -31
    );

    ctx.lineTo(
        108,
        -72
    );

    ctx.stroke();

    ctx.shadowBlur=0;

    ctx.strokeStyle=
        f.data.color;

    ctx.lineWidth=2;

    ctx.beginPath();

    ctx.moveTo(
        64,
        -32
    );

    ctx.lineTo(
        108,
        -72
    );

    ctx.stroke();

    ctx.restore();
}

/* =========================================================
   ATTACK POSE
========================================================= */

function drawAttackPose(
    f,
    x,
    y
){

    ctx.save();

    ctx.translate(
        x,
        y
    );

    ctx.scale(
        f.facing,
        1
    );

    const strong=
        f.state==="heavy";

    ctx.strokeStyle=
        f.data.color;

    ctx.lineWidth=
        strong
        ?8
        :5;

    ctx.globalAlpha=.75;

    ctx.shadowBlur=18;

    ctx.shadowColor=
        f.data.color;

    ctx.beginPath();

    ctx.arc(
        25,
        -28,
        strong
        ?95
        :70,
        strong
        ?-1.05
        :-.8,
        .55
    );

    ctx.stroke();

    ctx.restore();
}

/* =========================================================
   SKILL POSE
========================================================= */

function drawSkillPose(
    f,
    x,
    y
){

    ctx.save();

    ctx.translate(
        x,
        y
    );

    ctx.scale(
        f.facing,
        1
    );

    ctx.strokeStyle=
        f.data.color;

    ctx.lineWidth=5;

    ctx.globalAlpha=.75;

    ctx.shadowBlur=18;

    ctx.shadowColor=
        f.data.color;

    ctx.beginPath();

    ctx.moveTo(
        18,
        -20
    );

    ctx.lineTo(
        70,
        -45
    );

    ctx.stroke();

    ctx.restore();
}

/* =========================================================
   ULTIMATE POSE
========================================================= */

function drawUltimatePose(
    f,
    x,
    y
){

    ctx.save();

    ctx.translate(
        x,
        y
    );

    ctx.globalAlpha=.30;

    ctx.strokeStyle=
        f.data.color;

    ctx.lineWidth=7;

    ctx.shadowBlur=30;

    ctx.shadowColor=
        f.data.color;

    ctx.beginPath();

    ctx.arc(
        0,
        -40,
        105+
            Math.sin(
                f.anim*12
            )*12,
        0,
        Math.PI*2
    );

    ctx.stroke();

    ctx.globalAlpha=1;

    ctx.restore();
}

/* =========================================================
   SLASH
========================================================= */

function slash(
    x,
    y,
    color,
    facing,
    size,
    life
){

    slashes.push({

        x:x,
        y:y,
        color:color,
        facing:facing,
        size:size,
        life:life,
        max:life
    });
}

/* =========================================================
   PROJECTILE
========================================================= */

function drawProjectile(p){

    ctx.save();

    ctx.translate(
        p.x,
        p.y
    );

    p.rot+=.12;

    if(
        p.type==="water"
    ){

        ctx.fillStyle="#39d7ff";

        ctx.shadowBlur=25;
        ctx.shadowColor="#27bfff";

        ctx.beginPath();

        ctx.arc(
            0,
            0,
            p.size,
            0,
            Math.PI*2
        );

        ctx.fill();

        ctx.strokeStyle="#a8f5ff";
        ctx.lineWidth=4;

        ctx.beginPath();

        ctx.arc(
            0,
            0,
            p.size+7,
            p.rot,
            p.rot+4
        );

        ctx.stroke();

        ctx.beginPath();

        ctx.arc(
            0,
            0,
            p.size+13,
            -p.rot,
            -p.rot+2
        );

        ctx.stroke();

    }else if(
        p.type==="fire"
    ){

        ctx.fillStyle="#ff532d";

        ctx.shadowBlur=30;
        ctx.shadowColor="#ff4b25";

        ctx.beginPath();

        ctx.moveTo(
            -p.size,
            0
        );

        ctx.quadraticCurveTo(
            0,
            -p.size*1.5,
            p.size*1.4,
            0
        );

        ctx.quadraticCurveTo(
            0,
            p.size*1.2,
            -p.size,
            0
        );

        ctx.fill();

        ctx.fillStyle="#ffd05a";

        ctx.beginPath();

        ctx.arc(
            -5,
            0,
            p.size*.45,
            0,
            Math.PI*2
        );

        ctx.fill();

    }else if(
        p.type==="thunder"
    ){

        ctx.strokeStyle="#fff36c";

        ctx.shadowBlur=28;
        ctx.shadowColor="#ffe63d";

        ctx.lineWidth=7;

        ctx.beginPath();

        ctx.moveTo(
            -22,
            9
        );

        ctx.lineTo(
            -7,
            -12
        );

        ctx.lineTo(
            2,
            3
        );

        ctx.lineTo(
            20,
            -16
        );

        ctx.stroke();

        ctx.lineWidth=2;

        ctx.strokeStyle="#ffffff";

        ctx.stroke();

    }else if(
        p.type==="flower"
    ){

        ctx.fillStyle="#ff83cf";

        ctx.shadowBlur=22;
        ctx.shadowColor="#ff63bd";

        for(
            let i=0;
            i<6;
            i++
        ){

            const a=
                i*
                Math.PI*
                2/
                6+
                p.rot;

            ctx.beginPath();

            ctx.ellipse(
                Math.cos(a)*10,
                Math.sin(a)*10,
                9,
                15,
                a,
                0,
                Math.PI*2
            );

            ctx.fill();
        }

        ctx.fillStyle="#ffe66d";

        ctx.beginPath();

        ctx.arc(
            0,
            0,
            6,
            0,
            Math.PI*2
        );

        ctx.fill();

    }else if(
        p.type==="rock"
    ){

        ctx.fillStyle="#9f9277";

        ctx.shadowBlur=18;
        ctx.shadowColor="#a89a7d";

        ctx.rotate(
            p.rot
        );

        ctx.beginPath();

        ctx.moveTo(
            -22,
            -10
        );

        ctx.lineTo(
            -5,
            -22
        );

        ctx.lineTo(
            18,
            -11
        );

        ctx.lineTo(
            23,
            8
        );

        ctx.lineTo(
            3,
            20
        );

        ctx.lineTo(
            -20,
            12
        );

        ctx.closePath();

        ctx.fill();

    }else if(
        p.type==="wind"
    ){

        ctx.strokeStyle="#83ffe4";

        ctx.shadowBlur=30;
        ctx.shadowColor="#59efd0";

        ctx.lineWidth=6;

        for(
            let i=0;
            i<4;
            i++
        ){

            ctx.beginPath();

            ctx.arc(
                0,
                0,
                p.size-
                    i*7,
                -.9+
                    i*.2,
                1.1+
                    i*.2
            );

            ctx.stroke();
        }

        ctx.strokeStyle="#d5fff7";
        ctx.lineWidth=2;

        ctx.beginPath();

        ctx.moveTo(
            -30,
            0
        );

        ctx.quadraticCurveTo(
            0,
            -24,
            30,
            0
        );

        ctx.stroke();
    }

    ctx.restore();
}

/* =========================================================
   ULTIMATE EFFECT
========================================================= */

let ultimateTimer=0;
let ultimateFighter=null;

function ultimateEffect(f){

    ultimateTimer=1.15;

    ultimateFighter=f;

    ring(
        f.x,
        f.bodyY,
        f.data.color,
        200
    );

    particle(
        f.x,
        f.bodyY-50,
        f.data.color,
        90,
        430
    );

    /*
       Water
    */

    if(
        f.data.style===
        "water"
    ){

        for(
            let i=0;
            i<16;
            i++
        ){

            waterArcs.push({

                x:
                    f.x+
                    rand(-160,160),

                y:
                    f.bodyY+
                    rand(-150,50),

                life:1.4,

                rot:
                    rand(0,6)
            });
        }
    }

    /*
       Fire
    */

    if(
        f.data.style===
        "fire"
    ){

        for(
            let i=0;
            i<45;
            i++
        ){

            fireTrails.push({

                x:
                    f.x+
                    rand(-160,160),

                y:
                    f.bodyY+
                    rand(-130,60),

                vx:
                    rand(-180,180),

                life:
                    rand(.6,1.5)
            });
        }
    }

    /*
       Thunder
    */

    if(
        f.data.style===
        "thunder"
    ){

        for(
            let i=0;
            i<15;
            i++
        ){

            lightningBolts.push({

                x:
                    f.x+
                    rand(-200,200),

                y:
                    f.bodyY-
                    rand(30,220),

                life:
                    rand(.4,1)
            });
        }
    }

    /*
       Flower
    */

    if(
        f.data.style===
        "flower"
    ){

        for(
            let i=0;
            i<60;
            i++
        ){

            flowerPetals.push({

                x:
                    f.x+
                    rand(-210,210),

                y:
                    f.bodyY+
                    rand(-170,80),

                vx:
                    rand(-100,100),

                vy:
                    rand(-220,-30),

                rot:
                    rand(0,6),

                life:1.5
            });
        }
    }

    /*
       Rock
    */

    if(
        f.data.style===
        "rock"
    ){

        for(
            let i=0;
            i<35;
            i++
        ){

            rockChunks.push({

                x:
                    f.x+
                    rand(-180,180),

                y:
                    f.bodyY+
                    rand(-100,50),

                vx:
                    rand(-300,300),

                vy:
                    rand(-300,-70),

                life:
                    rand(.8,1.6)
            });
        }
    }

    /*
       Wind
    */

    if(
        f.data.style===
        "wind"
    ){

        for(
            let i=0;
            i<30;
            i++
        ){

            windBlades.push({

                x:
                    f.x+
                    rand(-180,180),

                y:
                    f.bodyY+
                    rand(-150,80),

                vx:
                    rand(-300,300),

                life:1.2,

                size:
                    rand(25,70),

                rot:
                    rand(-1,1)
            });
        }
    }
}

/* =========================================================
   WORLD
========================================================= */

function drawWorld(){

    const grad=
        ctx.createLinearGradient(
            0,
            0,
            0,
            H
        );

    grad.addColorStop(
        0,
        "#050714"
    );

    grad.addColorStop(
        .48,
        "#0a1030"
    );

    grad.addColorStop(
        1,
        "#15132b"
    );

    ctx.fillStyle=grad;

    ctx.fillRect(
        0,
        0,
        W,
        H
    );

    /* moon */

    const mx=W*.5;
    const my=130;

    ctx.save();

    ctx.shadowBlur=45;
    ctx.shadowColor=
        "rgba(160,200,255,.55)";

    ctx.fillStyle="#dceaff";

    ctx.beginPath();

    ctx.arc(
        mx,
        my,
        62,
        0,
        Math.PI*2
    );

    ctx.fill();

    ctx.restore();

    ctx.fillStyle="#101635";

    ctx.beginPath();

    ctx.arc(
        mx+23,
        my-14,
        59,
        0,
        Math.PI*2
    );

    ctx.fill();

    /* stars */

    for(
        let i=0;
        i<70;
        i++
    ){

        const sx=
            (i*173)%W;

        const sy=
            25+
            (i*67)%300;

        const tw=
            .35+
            Math.sin(
                performance.now()/
                500+
                i
            )*.25;

        ctx.globalAlpha=
            Math.max(
                .05,
                tw
            );

        ctx.fillStyle="#cde5ff";

        ctx.fillRect(
            sx,
            sy,
            2,
            2
        );
    }

    ctx.globalAlpha=1;

    /* clouds */

    for(
        let i=0;
        i<6;
        i++
    ){

        const cx=
            (i*300+80)-
            (
                performance.now()/
                1000*
                7
            )%350;

        const cy=
            185+
            (i%2)*55;

        ctx.fillStyle=
            "rgba(110,140,210,.07)";

        ctx.beginPath();

        ctx.ellipse(
            cx,
            cy,
            105,
            23,
            0,
            0,
            Math.PI*2
        );

        ctx.fill();

        ctx.beginPath();

        ctx.ellipse(
            cx+82,
            cy-8,
            82,
            19,
            0,
            0,
            Math.PI*2
        );

        ctx.fill();
    }

    /* city */

    for(
        let i=0;
        i<35;
        i++
    ){

        const bw=
            25+
            ((i*17)%60);

        const bh=
            40+
            ((i*43)%140);

        const bx=
            i*55;

        ctx.fillStyle="#080b1c";

        ctx.fillRect(
            bx,
            H-155-bh,
            bw,
            bh
        );

        ctx.fillStyle=
            "rgba(90,130,255,.14)";

        for(
            let wy=0;
            wy<5;
            wy++
        ){

            ctx.fillRect(
                bx+8,
                H-145-bh+
                    wy*20,
                4,
                7
            );
        }
    }

    /* floor */

    const floorY=
        H-150;

    const floorGrad=
        ctx.createLinearGradient(
            0,
            floorY,
            0,
            H
        );

    floorGrad.addColorStop(
        0,
        "#191d43"
    );

    floorGrad.addColorStop(
        1,
        "#080a18"
    );

    ctx.fillStyle=floorGrad;

    ctx.fillRect(
        0,
        floorY,
        W,
        H-floorY
    );

    ctx.strokeStyle=
        "rgba(100,170,255,.36)";

    ctx.lineWidth=2;

    ctx.beginPath();

    ctx.moveTo(
        0,
        floorY
    );

    ctx.lineTo(
        W,
        floorY
    );

    ctx.stroke();

    ctx.strokeStyle=
        "rgba(110,150,255,.08)";

    ctx.lineWidth=1;

    for(
        let x=0;
        x<W;
        x+=80
    ){

        ctx.beginPath();

        ctx.moveTo(
            x,
            floorY
        );

        ctx.lineTo(
            x+80,
            H
        );

        ctx.stroke();
    }

    for(
        let y=floorY+30;
        y<H;
        y+=30
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
}

/* =========================================================
   EFFECT UPDATE
========================================================= */

function updateEffects(dt){

    for(
        let i=particles.length-1;
        i>=0;
        i--
    ){

        const p=particles[i];

        p.life-=dt;

        p.x+=
            p.vx*dt;

        p.y+=
            p.vy*dt;

        p.vy+=
            300*dt;

        if(p.life<=0){

            particles.splice(
                i,
                1
            );
        }
    }

    for(
        let i=slashes.length-1;
        i>=0;
        i--
    ){

        const s=slashes[i];

        s.life-=dt;

        if(s.life<=0){

            slashes.splice(
                i,
                1
            );
        }
    }

    for(
        let i=shockwaves.length-1;
        i>=0;
        i--
    ){

        const s=shockwaves[i];

        s.life-=dt;

        s.r+=
            (s.max-s.r)*
            dt*
            8;

        if(s.life<=0){

            shockwaves.splice(
                i,
                1
            );
        }
    }

    for(
        let i=afterimages.length-1;
        i>=0;
        i--
    ){

        const a=afterimages[i];

        a.life-=dt;

        if(a.life<=0){

            afterimages.splice(
                i,
                1
            );
        }
    }

    for(
        let i=windBlades.length-1;
        i>=0;
        i--
    ){

        const b=windBlades[i];

        b.life-=dt;

        b.x+=
            b.vx*dt;

        b.y+=
            Math.sin(
                performance.now()/150+
                b.x
            )*
            20*
            dt;

        if(b.life<=0){

            windBlades.splice(
                i,
                1
            );
        }
    }

    for(
        let i=flowerPetals.length-1;
        i>=0;
        i--
    ){

        const p=flowerPetals[i];

        p.life-=dt;

        p.x+=
            p.vx*dt;

        p.y+=
            p.vy*dt;

        p.vy+=
            120*dt;

        p.rot+=
            dt*4;

        if(p.life<=0){

            flowerPetals.splice(
                i,
                1
            );
        }
    }

    for(
        let i=waterArcs.length-1;
        i>=0;
        i--
    ){

        const a=waterArcs[i];

        a.life-=dt;

        a.rot+=
            dt*2;

        if(a.life<=0){

            waterArcs.splice(
                i,
                1
            );
        }
    }

    for(
        let i=fireTrails.length-1;
        i>=0;
        i--
    ){

        const f=fireTrails[i];

        f.life-=dt;

        f.x+=
            f.vx*dt;

        if(f.life<=0){

            fireTrails.splice(
                i,
                1
            );
        }
    }

    for(
        let i=lightningBolts.length-1;
        i>=0;
        i--
    ){

        const l=lightningBolts[i];

        l.life-=dt;

        if(l.life<=0){

            lightningBolts.splice(
                i,
                1
            );
        }
    }

    for(
        let i=rockChunks.length-1;
        i>=0;
        i--
    ){

        const r=rockChunks[i];

        r.life-=dt;

        r.x+=
            r.vx*dt;

        r.y+=
            r.vy*dt;

        r.vy+=
            500*dt;

        if(r.life<=0){

            rockChunks.splice(
                i,
                1
            );
        }
    }

    if(ultimateTimer>0){

        ultimateTimer-=dt;

        if(
            ultimateTimer<=0
        ){

            ultimateFighter=null;
        }
    }
}

/* =========================================================
   DRAW EFFECTS
========================================================= */

function drawEffects(){

    /*
       afterimages
    */

    afterimages.forEach(
        function(a){

            ctx.save();

            ctx.globalAlpha=
                (a.life/a.max)*.22;

            ctx.translate(
                a.x,
                a.y
            );

            ctx.scale(
                a.facing,
                1
            );

            ctx.fillStyle=
                a.color;

            ctx.beginPath();

            ctx.ellipse(
                0,
                -40,
                31,
                65,
                0,
                0,
                Math.PI*2
            );

            ctx.fill();

            ctx.restore();
        }
    );

    /*
       projectiles
    */

    projectiles.forEach(
        drawProjectile
    );

    /*
       water arcs
    */

    waterArcs.forEach(
        function(a){

            ctx.save();

            ctx.globalAlpha=
                a.life/.7;

            ctx.strokeStyle="#8cefff";

            ctx.shadowBlur=20;
            ctx.shadowColor="#39cfff";

            ctx.lineWidth=4;

            ctx.beginPath();

            ctx.arc(
                a.x,
                a.y,
                35+
                    (1-a.life)*
                    80,
                a.rot,
                a.rot+2
            );

            ctx.stroke();

            ctx.restore();
        }
    );

    /*
       fire trails
    */

    fireTrails.forEach(
        function(f){

            ctx.save();

            ctx.globalAlpha=
                Math.min(
                    1,
                    f.life*2
                );

            ctx.fillStyle=
                f.life>.3
                ?"#ff8b30"
                :"#ff3e27";

            ctx.shadowBlur=18;
            ctx.shadowColor="#ff4b25";

            ctx.beginPath();

            ctx.arc(
                f.x,
                f.y,
                4+
                    f.life*7,
                0,
                Math.PI*2
            );

            ctx.fill();

            ctx.restore();
        }
    );

    /*
       lightning
    */

    lightningBolts.forEach(
        function(l){

            ctx.save();

            ctx.globalAlpha=
                Math.min(
                    1,
                    l.life*3
                );

            ctx.strokeStyle=
                "#fff78a";

            ctx.shadowBlur=25;
            ctx.shadowColor="#ffe84a";

            ctx.lineWidth=4;

            ctx.beginPath();

            ctx.moveTo(
                l.x-15,
                l.y-45
            );

            ctx.lineTo(
                l.x+5,
                l.y-12
            );

            ctx.lineTo(
                l.x-10,
                l.y+5
            );

            ctx.lineTo(
                l.x+20,
                l.y+42
            );

            ctx.stroke();

            ctx.restore();
        }
    );

    /*
       rocks
    */

    rockChunks.forEach(
        function(r){

            ctx.save();

            ctx.globalAlpha=
                Math.min(
                    1,
                    r.life*2
                );

            ctx.translate(
                r.x,
                r.y
            );

            ctx.rotate(
                r.life*4
            );

            ctx.fillStyle="#a99a7e";

            ctx.beginPath();

            ctx.moveTo(
                -8,
                -6
            );

            ctx.lineTo(
                5,
                -10
            );

            ctx.lineTo(
                10,
                4
            );

            ctx.lineTo(
                -4,
                9
            );

            ctx.closePath();

            ctx.fill();

            ctx.restore();
        }
    );

    /*
       slash
    */

    slashes.forEach(
        function(s){

            ctx.save();

            ctx.translate(
                s.x,
                s.y
            );

            ctx.scale(
                s.facing,
                1
            );

            ctx.globalAlpha=
                s.life/
                s.max;

            ctx.strokeStyle=
                s.color;

            ctx.shadowBlur=25;

            ctx.shadowColor=
                s.color;

            ctx.lineWidth=7;

            ctx.beginPath();

            ctx.arc(
                15,
                -30,
                s.size,
                -.95,
                .55
            );

            ctx.stroke();

            ctx.lineWidth=2;

            ctx.strokeStyle="#ffffff";

            ctx.stroke();

            ctx.restore();
        }
    );

    /*
       shockwaves
    */

    shockwaves.forEach(
        function(s){

            ctx.save();

            ctx.globalAlpha=
                s.life/.45;

            ctx.strokeStyle=
                s.color;

            ctx.shadowBlur=25;

            ctx.shadowColor=
                s.color;

            ctx.lineWidth=4;

            ctx.beginPath();

            ctx.arc(
                s.x,
                s.y,
                s.r,
                0,
                Math.PI*2
            );

            ctx.stroke();

            ctx.restore();
        }
    );

    /*
       wind blades
    */

    windBlades.forEach(
        function(b){

            ctx.save();

            ctx.globalAlpha=
                Math.min(
                    1,
                    b.life*2
                );

            ctx.translate(
                b.x,
                b.y
            );

            ctx.rotate(
                b.rot
            );

            ctx.strokeStyle=
                "#8dffe9";

            ctx.shadowBlur=22;

            ctx.shadowColor=
                "#5cf2d1";

            ctx.lineWidth=5;

            ctx.beginPath();

            ctx.arc(
                0,
                0,
                b.size,
                -.9,
                .8
            );

            ctx.stroke();

            ctx.restore();
        }
    );

    /*
       petals
    */

    flowerPetals.forEach(
        function(p){

            ctx.save();

            ctx.globalAlpha=
                Math.min(
                    1,
                    p.life
                );

            ctx.translate(
                p.x,
                p.y
            );

            ctx.rotate(
                p.rot
            );

            ctx.fillStyle=
                "#ff91d4";

            ctx.shadowBlur=10;

            ctx.shadowColor=
                "#ff63bd";

            ctx.beginPath();

            ctx.ellipse(
                0,
                0,
                5,
                10,
                0,
                0,
                Math.PI*2
            );

            ctx.fill();

            ctx.restore();
        }
    );

    /*
       particles
    */

    particles.forEach(
        function(p){

            ctx.save();

            ctx.globalAlpha=
                Math.max(
                    0,
                    p.life
                );

            ctx.fillStyle=
                p.color;

            ctx.shadowBlur=10;

            ctx.shadowColor=
                p.color;

            ctx.beginPath();

            ctx.arc(
                p.x,
                p.y,
                p.size,
                0,
                Math.PI*2
            );

            ctx.fill();

            ctx.restore();
        }
    );

    /*
       ultimate
    */

    if(
        ultimateTimer>0&&
        ultimateFighter
    ){

        const f=
            ultimateFighter;

        ctx.save();

        ctx.globalAlpha=
            Math.min(
                .48,
                ultimateTimer*.45
            );

        ctx.strokeStyle=
            f.data.color;

        ctx.lineWidth=9;

        ctx.shadowBlur=35;

        ctx.shadowColor=
            f.data.color;

        ctx.beginPath();

        ctx.arc(
            f.x,
            f.bodyY-45,
            175+
                (1.15-
                ultimateTimer)*
                100,
            0,
            Math.PI*2
        );

        ctx.stroke();

        ctx.restore();

        if(
            f.data.style===
            "wind"
        ){

            ctx.save();

            ctx.globalAlpha=.55;

            ctx.strokeStyle=
                "#9ffff0";

            ctx.shadowBlur=30;

            ctx.shadowColor=
                "#63f5d8";

            ctx.lineWidth=5;

            for(
                let i=0;
                i<10;
                i++
            ){

                ctx.beginPath();

                ctx.arc(
                    f.x,
                    f.bodyY-40,
                    85+i*20,
                    i*.7+
                        ultimateTimer,
                    i*.7+
                        ultimateTimer+
                        1.8
                );

                ctx.stroke();
            }

            ctx.restore();
        }
    }
}

/* =========================================================
   PROJECTILE UPDATE
========================================================= */

function updateProjectiles(dt){

    for(
        let i=projectiles.length-1;
        i>=0;
        i--
    ){

        const p=
            projectiles[i];

        p.life-=dt;

        p.x+=
            p.vx*dt;

        p.rot+=
            dt*5;

        const target=
            p.owner===player2
            ?player1
            :player2;

        if(
            Math.abs(
                p.x-
                target.x
            )<48&&
            Math.abs(
                p.y-
                target.bodyY
            )<75
        ){

            target.takeDamage(
                p.damage,
                Math.sign(
                    p.vx
                )
            );

            particle(
                p.x,
                p.y,
                p.owner.data.color,
                20,
                180
            );

            ring(
                p.x,
                p.y,
                p.owner.data.color,
                42
            );

            projectiles.splice(
                i,
                1
            );

            continue;
        }

        if(
            p.life<=0||
            p.x<-120||
            p.x>W+120
        ){

            projectiles.splice(
                i,
                1
            );
        }
    }
}

/* =========================================================
   GAME STATE
========================================================= */

let player1=null;
let player2=null;

let gameStarted=false;
let running=false;
let ending=false;

let timeLeft=60;

let lastTime=
    performance.now();

/* =========================================================
   START
========================================================= */

function startGame(){

    initAudio();

    const n1=
        document
        .getElementById("p1Name")
        .value
        .trim()
        .substring(
            0,
            20
        )||
        "Player 1";

    const n2=
        document
        .getElementById("p2Name")
        .value
        .trim()
        .substring(
            0,
            20
        )||
        "Player 2";

    player1=
        new Fighter(
            W*.30,
            1,
            selectedP1
        );

    player2=
        new Fighter(
            W*.70,
            2,
            gameMode==="cpu"
            ?getRandomEnemy(
                selectedP1
            )
            :selectedP2
        );

    player1.name=n1;

    player2.name=
        gameMode==="cpu"
        ?"CPU • HARD"
        :n2;

    gameStarted=true;

    running=false;

    ending=false;

    timeLeft=60;

    home.classList.add(
        "hidden"
    );

    hud.classList.remove(
        "hidden"
    );

    help.classList.remove(
        "hidden"
    );

    result.classList.add(
        "hidden"
    );

    name1El.textContent=
        player1.name+
        " • "+
        player1.data.name;

    name2El.textContent=
        player2.name+
        " • "+
        player2.data.name;

    countdown();
}

function getRandomEnemy(
    except
){

    const ids=
        Object.keys(
            CHARACTERS
        ).filter(
            function(x){
                return x!==except;
            }
        );

    return ids[
        Math.floor(
            Math.random()*
            ids.length
        )
    ];
}

/* =========================================================
   COUNTDOWN
========================================================= */

function countdown(){

    countdownEl.classList.remove(
        "hidden"
    );

    const nums=[
        "3",
        "2",
        "1",
        "FIGHT!"
    ];

    let i=0;

    countdownEl.textContent=
        nums[i];

    sfxCountdown(3);

    const interval=
        setInterval(
            function(){

                i++;

                if(
                    i>=nums.length
                ){

                    clearInterval(
                        interval
                    );

                    sfxFight();

                    setTimeout(
                        function(){

                            countdownEl.classList.add(
                                "hidden"
                            );

                            running=true;

                        },
                        500
                    );

                    return;
                }

                countdownEl.textContent=
                    nums[i];

                if(
                    nums[i]==="2"
                ){

                    sfxCountdown(2);
                }

                if(
                    nums[i]==="1"
                ){

                    sfxCountdown(1);
                }

            },
            650
        );
}

/* =========================================================
   END
========================================================= */

function endGame(){

    if(!gameStarted)
        return;

    if(ending)
        return;

    ending=true;

    running=false;

    let winner=null;

    if(
        player1.hp<=0&&
        player2.hp<=0
    ){

        resultTitle.textContent=
            "DRAW";

        resultSub.textContent=
            "Cả hai đã chiến đấu đến cùng!";

        sfxDraw();

    }else if(
        player1.hp<=0
    ){

        winner=player2;

        resultTitle.textContent=
            gameMode==="cpu"
            ?"YOU LOSE"
            :"PLAYER 2 VICTORY";

        resultSub.textContent=
            winner.name+
            " • "+
            winner.data.name+
            " thắng trận!";

        sfxDefeat();

    }else if(
        player2.hp<=0
    ){

        winner=player1;

        resultTitle.textContent=
            "VICTORY";

        resultSub.textContent=
            winner.name+
            " • "+
            winner.data.name+
            " đã chiến thắng!";

        sfxVictory();

        createBalloons();

    }else{

        if(
            player1.hp>
            player2.hp
        ){

            winner=player1;

            resultTitle.textContent=
                "VICTORY";

            resultSub.textContent=
                winner.name+
                " thắng nhờ HP cao hơn!";

            sfxVictory();

            createBalloons();

        }else if(
            player2.hp>
            player1.hp
        ){

            winner=player2;

            resultTitle.textContent=
                gameMode==="cpu"
                ?"YOU LOSE"
                :"PLAYER 2 VICTORY";

            resultSub.textContent=
                winner.name+
                " thắng nhờ HP cao hơn!";

            sfxDefeat();

        }else{

            resultTitle.textContent=
                "DRAW";

            resultSub.textContent=
                "Hai bên hòa!";

            sfxDraw();
        }
    }

    result.classList.remove(
        "hidden"
    );
}

/* =========================================================
   BALLOONS
========================================================= */

function createBalloons(){

    balloons.innerHTML="";

    const colors=[
        "#ff4f7b",
        "#5cc8ff",
        "#ffd84f",
        "#7aff9a",
        "#c57aff",
        "#ff8c54"
    ];

    for(
        let i=0;
        i<35;
        i++
    ){

        const b=
            document.createElement(
                "div"
            );

        b.className=
            "balloon";

        b.style.left=
            Math.random()*
            100+
            "%";

        b.style.background=
            colors[
                Math.floor(
                    Math.random()*
                    colors.length
                )
            ];

        b.style.color=
            b.style.background;

        b.style.animationDelay=
            Math.random()*
            1.6+
            "s";

        b.style.transform=
            "scale("+
            (
                .7+
                Math.random()*
                .7
            )+
            ")";

        balloons.appendChild(b);
    }
}

/* =========================================================
   BUTTONS
========================================================= */

document.getElementById(
    "startBtn"
).onclick=
    startGame;

document.getElementById(
    "backBtn"
).onclick=
    function(){

        gameStarted=false;

        running=false;

        ending=false;

        result.classList.add(
            "hidden"
        );

        hud.classList.add(
            "hidden"
        );

        help.classList.add(
            "hidden"
        );

        home.classList.remove(
            "hidden"
        );

        countdownEl.classList.add(
            "hidden"
        );

        balloons.innerHTML="";

        particles.length=0;
        projectiles.length=0;
        slashes.length=0;
        shockwaves.length=0;
        afterimages.length=0;
        windBlades.length=0;
        flowerPetals.length=0;
        lightningBolts.length=0;
        fireTrails.length=0;
        waterArcs.length=0;
        rockChunks.length=0;

        player1=null;
        player2=null;
    };

/* =========================================================
   HUD
========================================================= */

function updateHUD(){

    if(
        !player1||
        !player2
    )
        return;

    hp1El.style.width=
        clamp(
            player1.hp,
            0,
            100
        )+
        "%";

    hp2El.style.width=
        clamp(
            player2.hp,
            0,
            100
        )+
        "%";

    energy1El.style.width=
        clamp(
            player1.energy,
            0,
            100
        )+
        "%";

    energy2El.style.width=
        clamp(
            player2.energy,
            0,
            100
        )+
        "%";

    timerEl.textContent=
        Math.ceil(
            timeLeft
        );
}

/* =========================================================
   GAME LOOP
========================================================= */

function gameLoop(now){

    const dt=
        Math.min(
            .033,
            (now-lastTime)/1000
        );

    lastTime=now;

    drawWorld();

    updateEffects(dt);

    if(gameStarted){

        if(running){

            player1.update(
                dt,
                player2
            );

            player2.update(
                dt,
                player1
            );

            updateProjectiles(dt);

            timeLeft-=dt;

            if(
                timeLeft<=0
            ){

                timeLeft=0;

                endGame();
            }

            if(
                !ending&&
                (
                    player1.dead||
                    player2.dead
                )
            ){

                running=false;

                setTimeout(
                    function(){

                        endGame();

                    },
                    350
                );
            }
        }

        drawEffects();

        if(player1){

            player1.draw();
        }

        if(player2){

            player2.draw();
        }

        updateHUD();

    }else{

        drawEffects();
    }

    requestAnimationFrame(
        gameLoop
    );
}

requestAnimationFrame(
    gameLoop
);

</script>

</div>

</body>
</html>
"""

components.html(
    HTML,
    height=900,
    scrolling=True
)
