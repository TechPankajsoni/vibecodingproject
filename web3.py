
from http.server import HTTPServer, BaseHTTPRequestHandler

HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Spider Web | Personal Links</title>

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    min-height: 100vh;
    overflow: hidden;
    display: flex;
    justify-content: center;
    align-items: center;
    font-family: Arial, sans-serif;
    color: white;

    background:
        radial-gradient(circle at 15% 20%, #e52435 0%, transparent 35%),
        radial-gradient(circle at 85% 80%, #0648a9 0%, transparent 40%),
        linear-gradient(135deg, #080b19, #101d40, #080b19);

    perspective: 1200px;
}

/* Animated background */

body::before {
    content: "";
    position: fixed;
    inset: -50%;
    pointer-events: none;

    background:
        repeating-radial-gradient(
            circle at 50% 50%,
            transparent 0 48px,
            rgba(255,255,255,.12) 49px 50px
        ),
        repeating-conic-gradient(
            from 0deg,
            transparent 0deg 14deg,
            rgba(255,255,255,.12) 14.2deg 14.5deg,
            transparent 14.7deg 30deg
        );

    animation: webRotate 50s linear infinite;
    opacity: .35;
}

@keyframes webRotate {
    to { transform: rotate(360deg); }
}

/* Floating decorations */

.spider {
    position: fixed;
    font-size: 45px;
    filter: drop-shadow(0 0 12px #ff1e36);
    animation: spiderFloat 6s ease-in-out infinite;
    z-index: 0;
    pointer-events: none;
}

.spider.one {
    top: 10%;
    left: 12%;
}

.spider.two {
    bottom: 12%;
    right: 12%;
    animation-delay: 2s;
    font-size: 55px;
}

.spider.three {
    top: 20%;
    right: 20%;
    font-size: 25px;
    animation-delay: 1s;
}

@keyframes spiderFloat {
    0%, 100% {
        transform: translateY(0) rotate(0deg);
    }
    50% {
        transform: translateY(45px) rotate(20deg);
    }
}

/* Main card */

.container {
    position: relative;
    z-index: 2;
    width: 440px;
    max-width: 92%;
    padding: 25px;
    border-radius: 20px;

    background: linear-gradient(
        145deg,
        rgba(220,25,48,.25),
        rgba(10,40,100,.55),
        rgba(15,20,45,.85)
    );

    border: 1px solid rgba(255,255,255,.25);

    backdrop-filter: blur(20px);

    box-shadow:
        0 25px 60px rgba(0,0,0,.6),
        0 0 20px rgba(255,25,50,.25),
        inset 0 1px 2px rgba(255,255,255,.3);

    transform-style: preserve-3d;
    animation: cardEntrance 1.2s ease,
               cardGlow 4s infinite alternate;

    transition: transform .15s ease;
}

@keyframes cardEntrance {
    from {
        opacity: 0;
        transform: translateY(80px) rotateX(25deg) scale(.7);
    }
    to {
        opacity: 1;
        transform: translateY(0) rotateX(0) scale(1);
    }
}

@keyframes cardGlow {
    0% {
        box-shadow: 0 0 15px #e52435;
    }
    100% {
        box-shadow: 0 0 35px #167bff,
                    0 0 55px rgba(229,36,53,.5);
    }
}

/* Heading */

.logo {
    text-align: center;
    margin-bottom: 25px;
    transform: translateZ(60px);
}

.logo .icon {
    font-size: 65px;
    display: block;
    animation: logoMove 3s ease-in-out infinite;
    filter: drop-shadow(0 0 15px #ff263e);
}

.logo h1 {
    font-size: 24px;
    letter-spacing: 3px;
    margin-top: 8px;
    color: #fff;
    text-shadow: 0 0 10px #ff233d,
                 0 0 20px #147bff;
}

.logo p {
    color: #c5d8ff;
    font-size: 11px;
    margin-top: 7px;
}

@keyframes logoMove {
    0%, 100% {
        transform: translateY(0) rotate(-5deg);
    }
    50% {
        transform: translateY(-12px) rotate(5deg);
    }
}

/* Links */

#links {
    display: flex;
    flex-direction: column;
    gap: 12px;
}

.link {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 13px;

    background: linear-gradient(
        110deg,
        rgba(235,35,55,.35),
        rgba(20,80,180,.35)
    );

    border: 1px solid rgba(255,255,255,.2);
    border-radius: 10px;

    transform: translateZ(30px);
    transition: .35s;
    animation: linkEnter .6s ease both;
}

@keyframes linkEnter {
    from {
        opacity: 0;
        transform: translateX(-40px) translateZ(0);
    }
    to {
        opacity: 1;
        transform: translateX(0) translateZ(30px);
    }
}

.link:hover {
    transform: translateZ(65px) scale(1.04);
    background: linear-gradient(110deg, #e52339, #0756c9);
    box-shadow:
        0 0 15px #ff263e,
        0 0 25px #126bff;
}

.link a {
    color: white;
    font-size: 14px;
    font-weight: bold;
    text-decoration: none;
    flex: 1;
}

.link a:hover {
    text-shadow: 0 0 10px white;
}

/* Buttons */

button {
    cursor: pointer;
    border: none;
    color: white;
    transition: .3s;
}

.delete {
    padding: 8px 11px;
    border-radius: 7px;

    background: linear-gradient(145deg, #ff5364, #a90021);

    box-shadow: 0 4px 0 #690015,
                0 0 10px #ff334f;
}

.delete:hover {
    transform: translateY(-4px) rotate(-8deg) scale(1.12);
    box-shadow: 0 8px 0 #690015,
                0 0 20px #ff334f;
}

.delete:active {
    transform: translateY(3px);
    box-shadow: 0 1px 0 #690015;
}

/* Input section */

.form {
    display: flex;
    gap: 8px;
    margin-top: 20px;
    transform: translateZ(45px);
}

input {
    width: 50%;
    min-width: 0;
    padding: 11px;

    border-radius: 7px;
    border: 1px solid rgba(255,255,255,.3);

    background: rgba(255,255,255,.95);
    color: #111;
    outline: none;
    font-size: 11px;

    transition: .3s;
}

input:focus {
    transform: translateY(-4px);
    border-color: #ff314b;
    box-shadow: 0 0 15px #ff314b;
}

/* Add button */

.add {
    padding: 10px 13px;
    border-radius: 7px;

    background: linear-gradient(145deg, #ff3b53, #a50022);

    font-weight: bold;
    font-size: 11px;

    box-shadow: 0 5px 0 #650016,
                0 0 12px #ff233d;
}

.add:hover {
    transform: translateY(-5px) scale(1.08);
    background: linear-gradient(145deg, #126dff, #00358d);

    box-shadow: 0 8px 0 #001c55,
                0 0 20px #167bff;
}

.add:active {
    transform: translateY(3px);
    box-shadow: 0 1px 0 #650016;
}

/* Footer */

.footer {
    text-align: center;
    font-size: 10px;
    color: #c5d8ff;
    margin-top: 20px;
    letter-spacing: 1px;
}

/* Mobile */

@media(max-width: 480px) {
    .container {
        padding: 18px;
    }

    .form {
        flex-wrap: wrap;
    }

    input {
        flex: 1 1 40%;
    }

    .add {
        width: 100%;
    }
}

/* Reduced motion */

@media(prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        animation-duration: .01ms !important;
        animation-iteration-count: 1 !important;
    }
}
</style>
</head>

<body>

<div class="spider one">🕷️</div>
<div class="spider two">🕸️</div>
<div class="spider three">🕷️</div>

<div class="container" id="card">

    <div class="logo">
        <span class="icon">🕷️</span>
        <h1>SPIDER LINKS</h1>
        <p>YOUR FRIENDLY NEIGHBOURHOOD QUICK LINKS</p>
    </div>

    <div id="links"></div>

    <form class="form" id="form">

        <input
            type="text"
            id="name"
            placeholder="Website Name"
            required
        >

        <input
            type="url"
            id="url"
            placeholder="https://example.com"
            required
        >

        <button class="add" type="submit">
            + ADD
        </button>

    </form>

    <div class="footer">
        🕸️ WITH GREAT LINKS COMES GREAT RESPONSIBILITY
    </div>

</div>

<script>

/* Default websites */

const defaultLinks = [
    {
        name: "YouTube",
        url: "https://www.youtube.com",
        emoji: "▶️"
    },
    {
        name: "Google",
        url: "https://www.google.com",
        emoji: "🔎"
    },
    {
        name: "Netflix",
        url: "https://www.netflix.com",
        emoji: "🎬"
    }
];

let websites;

try {
    const saved = localStorage.getItem("myLinks");

    websites = saved === null
        ? defaultLinks
        : JSON.parse(saved);

    if (!Array.isArray(websites)) {
        websites = defaultLinks;
    }
} catch {
    websites = defaultLinks;
}

/* Display websites */

function displayLinks() {

    const container = document.getElementById("links");

    container.replaceChildren();

    websites.forEach((site, index) => {

        const div = document.createElement("div");
        div.className = "link";

        const a = document.createElement("a");

        a.href = site.url;
        a.target = "_blank";
        a.rel = "noopener noreferrer";
        a.textContent = (site.emoji || "🔗") + " " + site.name;

        const btn = document.createElement("button");

        btn.className = "delete";
        btn.textContent = "🗑";
        btn.title = "Remove website";

        btn.onclick = function() {

            div.style.opacity = "0";
            div.style.transform = "translateX(50px) scale(.7)";

            setTimeout(() => {
                websites.splice(index, 1);
                saveLinks();
            }, 250);
        };

        div.appendChild(a);
        div.appendChild(btn);

        container.appendChild(div);
    });
}

/* Save websites */

function saveLinks() {

    localStorage.setItem(
        "myLinks",
        JSON.stringify(websites)
    );

    displayLinks();
}

/* Add website */

document.getElementById("form").onsubmit =
function(event) {

    event.preventDefault();

    const name = document.getElementById("name").value.trim();
    const url = document.getElementById("url").value.trim();

    try {

        const parsed = new URL(url);

        if (!["http:", "https:"].includes(parsed.protocol)) {
            alert("Enter a valid website URL!");
            return;
        }

        let emoji = "🔗";

        if (name.toLowerCase().includes("youtube")) {
            emoji = "▶️";
        }
        else if (name.toLowerCase().includes("google")) {
            emoji = "🔎";
        }
        else if (name.toLowerCase().includes("netflix")) {
            emoji = "🎬";
        }

        websites.push({
            name: name,
            url: parsed.href,
            emoji: emoji
        });

        saveLinks();

        this.reset();

    } catch {
        alert("Please enter a valid URL!");
    }
};

/* 3D mouse effect */

const card = document.getElementById("card");

card.addEventListener("mousemove", function(event) {

    const rect = card.getBoundingClientRect();

    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;

    const rotateX = (rect.height / 2 - y) / 22;
    const rotateY = (x - rect.width / 2) / 22;

    card.style.animation = "none";

    card.style.transform =
        `rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(1.03)`;
});

card.addEventListener("mouseleave", function() {

    card.style.transform =
        "rotateX(0deg) rotateY(0deg) scale(1)";

    card.style.animation =
        "cardGlow 4s infinite alternate";
});

/* Start */

displayLinks();

</script>

</body>
</html>
"""


class MyWebsite(BaseHTTPRequestHandler):

    def do_GET(self):

        self.send_response(200)

        self.send_header(
            "Content-type",
            "text/html; charset=utf-8"
        )

        self.end_headers()

        self.wfile.write(HTML.encode("utf-8"))


server = HTTPServer(("127.0.0.1", 8000), MyWebsite)

print("SPIDER LINKS WEBSITE STARTED!")
print("Open: http://127.0.0.1:8000")

try:
    server.serve_forever()
except KeyboardInterrupt:
    server.server_close()
    print("Server stopped!")
