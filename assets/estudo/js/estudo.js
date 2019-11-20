/* Essas primeiras funções controlam o comportamento do seletor de opções */

function changeTab(panel, id, max) {
    var tabActive = document.getElementById(panel + "-data-panel-" + id);
    tabActive.classList.remove("hidden");
    var panelActive = document.getElementById(panel + "-list-group-item-" + id);
    panelActive.classList.add("active");
    
    var i;
    for (i = 1; i <= max; i++) {
        if (i != id) {
            var tabNonActive = document.getElementById(panel + "-data-panel-" + i);
            tabNonActive.classList.add("hidden");
            var panelNonActive = document.getElementById(panel + "-list-group-item-" + i);
            panelNonActive.classList.remove("active");
        }
    }
}
