const hero = document.querySelector(".image-hero")

const tl = new TimelineMax();
tl.fromTo(
        hero,
        1,
        {height:"0%"},
        {height:"100%", ease:Power2.easeInOut}
    ).fromTo(
        hero,
        1.2,
        {width:"100%"},
        {width:"95%", ease:Power2.easeInOut}
    );


$('.carousel').carousel({
    interval: 100
    })