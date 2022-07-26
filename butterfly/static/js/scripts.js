window.onload = function() {
    let menu = document.querySelector(".menu");
    let dropMenu = document.querySelector(".dropdown");

    console.log(menu)
    console.log(dropMenu)

    function openDropMenu() {
        dropMenu.style.display = "flex";
        dropMenu.style.overflow = "visible";
    }
    function closeDropMenu() {
        dropMenu.style.display = "none";
        dropMenu.style.overflow = "hidden";
    }
    menu.addEventListener("mouseenter", openDropMenu);
    dropMenu.addEventListener("mouseleave", closeDropMenu);
}