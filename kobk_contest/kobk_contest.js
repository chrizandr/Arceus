function img_find() {
    var imgs = document.getElementsByTagName("img");
    var imgSrcs = [];

    for (var i = 0; i < imgs.length; i++) {
        imgSrcs.push(imgs[i].src);
    }

    return imgSrcs;
}

function img_filter(images) {
    var dex_numbers = [];
    for (let i = 0; i < images.length; i++) {
        const element = images[i];
        if (element.includes("graphics.tppcrpg.net/")){
            var items = element.split("/")
            var dex_id = items[items.length - 1].replace(".gif", " ").replace("M", "").replace("F", "").trim();
            dex_numbers.push(dex_id)
        }
    }
    return dex_numbers
}

var images = img_find()
dex_numbers = img_filter(images)