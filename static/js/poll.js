// Calculates the percentage of votes of the total votes this 
// choice has and sets the progressbar width accordingly
function setProgressBar(productVotes, totalVotes, productID) {
    var progressPercentage = Math.round(productVotes/totalVotes * 100);
    document.getElementById(productID).style.width = progressPercentage+"%";
}