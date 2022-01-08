// const { dialog } = require("electron");
// const path = require("electron");
const { ipcRenderer } = require("electron");
const fs = require("fs");
const path = require("path");

const wait = (ms) => {
  const start = Date.now();
  let now = start;
  while (now - start < ms) {
    now = Date.now();
  }
};

let directory;

function setSlideshow() {
  const files = fs.readdirSync(directory);

  document.getElementById("info").classList.add("hidden");

  const chosenFile = files[Math.floor(Math.random() * files.length)];
  document.getElementById("content").src = path.join(directory, chosenFile);

  setInterval(() => {
    const chosenFile = files[Math.floor(Math.random() * files.length)];
    document.getElementById("content").src = path.join(directory, chosenFile);
  }, 2000);
}

function selectDir() {
  ipcRenderer.send("file-open", "true");

  ipcRenderer.on("file-result", (event, arg) => {
    directory = arg.toString();
    setSlideshow();
  });
}

document.getElementById("selectbtn").addEventListener("click", () => {
  selectDir();
});
