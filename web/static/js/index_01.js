// 側邊面板
const menuButton = document.getElementById("hamburger-btn");
const sidebar = document.getElementById("sidebar");
let isSidebarOpen = false;

function toggleSidebar() {
    if (window.matchMedia("(max-width: 450px)").matches) {
        sidebar.style.width = (sidebar.style.width === "100vw") ? "0" : "100vw";
    } else {
        sidebar.style.width = (sidebar.style.width === "190px") ? "0" : "190px";
    }
}

function applyResponsiveEffect() {
    menuButton.removeEventListener("click", toggleSidebar);
    menuButton.addEventListener("click", toggleSidebar);

}

// 頁面載入完成時套用一次效果
applyResponsiveEffect();

// 監聽視窗大小變化，套用適當的效果
window.addEventListener('resize', applyResponsiveEffect);

// 選項點擊時的處理
const dropdownItems = document.querySelectorAll(".dropdown-item");
