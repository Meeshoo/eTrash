var playerElements = document.querySelectorAll(".player");

// console.log(playerElements);

playerElements.forEach(element => {
    console.log(element.id);
    element.addEventListener('click', function(event) {

        var playerCardWrapper = document.getElementById("player-card-wrapper");
        var playerCardBlock = document.getElementById("player-cards");
        var playerCards = document.querySelectorAll(".player-card");
        var arrow = document.getElementById("arrow");

        if (element.id == "mitch-player-info") {
            var playerCard = document.getElementById("mitch-player-card");
            arrow.style.marginLeft = "9%";
        }
        else if (element.id == "default-player-info") {
            var playerCard = document.getElementById("default-player-card");
            arrow.style.marginLeft = "29%";
        }
        else if (element.id == "callum-player-info") {
            var playerCard = document.getElementById("callum-player-card");
            arrow.style.marginLeft = "49%";
        }
        else if (element.id == "scanner-player-info") {
            var playerCard = document.getElementById("scanner-player-card");
            arrow.style.marginLeft = "69%";
        }
        else if (element.id == "jake-player-info") {
            var playerCard = document.getElementById("jake-player-card");
            arrow.style.marginLeft = "89%";
        }

        playerCardWrapper.style.display = "none";
        arrow.style.display = "none";
        playerCardBlock.style.display = "none";
        playerCards.forEach(element => {
            element.style.display = 'none';
        });

        playerCardWrapper.style.display = "flex";
        arrow.style.display = "block";
        playerCardBlock.style.display = "flex";
        playerCard.style.display = "flex";
      });
});