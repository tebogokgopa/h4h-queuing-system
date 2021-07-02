var images = [ 
    "../static/images/pic-1.jpg", 
    "../static/images/pic-2.jpg",
    "../static/images/pic.jpg"
];
var num = 0;
function next() {
    var slider = document.getElementById('imgHome');
    num++;
    if(num >= images.length) {
        num = 0;
    }
    slider.src = images[num];
}
function prev() {
    var slider = document.getElementById('imgHome');
    num--;
    if(num < 0) {
        num = images.length-1;
    }
    slider.src = images[num];
}

