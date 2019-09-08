<template>
<div>
  <head>
    <meta charset="UTF-8">
    <title>Sample</title>
    <script src="https://unpkg.com/leaflet@1.5.1/dist/leaflet.js"
            integrity="sha512-GffPMF3RvMeYyc1LWMHtK8EbPv0iNZ8/oTtHPx9/cc2ILxQ+u905qIwdpULaqDkyBKgOaB57QTMg7ztg8Jm2Og=="
            crossorigin=""></script>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.5.1/dist/leaflet.css"
          integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ=="
          crossorigin=""/>
<!--    <link rel="stylesheet" href="leaflet.css" crossorigin=""/>-->
<!--    <link rel="stylesheet" type="text/css" href="style.css">-->
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
    <script src="leaflet-src.js" crossorigin=""></script>
    <script src="promise.js"></script>
    <script src="base64.js"></script>
</head>
<body>
<div id="mapid"></div>
<img id="Picture">
</body>
</div>

</template>

<script>

 // if(L)
    // var mymap = L.map('mapid').setView([51.505, -0.09], 13);

    // L.marker([51.505, -0.09]).addTo(mymap);
    // L.geoJSON(data, {
    //     style: function (feature) {
    //         return {color: feature.properties.color};
    //     }
    // }).bindPopup(function (layer) {
    //     return layer.feature.properties.description;
    // }).addTo(map);
    // L.geoJSON("fake.json").addTo(mymap);
    // pointToLayer()


    ///example
    // axios({
    //     url: 'https://www.thecocktaildb.com/drink.php?c=11844-New-York-Sour',
    //     method: 'get'
    // })

    // receive= axios.get('https://www.thecocktaildb.com/drink.php?c=11844-New-York-Sour');
    // // document.write(receive.);
    // console.log(receive.data);
    // var cX;
    // var cY;
    // function init() {
    //     // if (window.Event) {
    //     //     document.captureEvents(Event.MOUSEMOVE);
    //     // }
    //     // document.onmousemove = getCursorXY;
    //     document.getElementById("Picture").onclick=function(){
    //         document.getElementById("Picture").style.display="none";
    //         alert('???')
    //     };
    //
    // }

    // function getCursorXY(e) {
    //     CursorX = (window.Event) ? e.pageX : event.clientX;
    //     CursorY = (window.Event) ? e.pageY : event.clientY;
    //     alert(CursorX)
    // }

    window.onload = function(){
        // alert('load complete')
        document.getElementById("Picture").onclick=function(){
            document.getElementById("Picture").style.display="none";
    };
        getAPI();
    }

    // alert(receive.toString());



    // ]).addTo(mymap).bindPopup("I am a polygon.");


    var popup = L.popup();


    function onMapClick(e) {
        popup
             .setLatLng(e.latlng)
             .setContent("You clicked the map at " + e.latlng.toString())
            .openOn(mymap);
    }
    // imageBounds = [center, [-35.8650, 154.2094]];

    // L.imageOverlay(imageUrl, imageBounds).addTo(map);
    // L.imageOverlay(imageUrl, imageBounds).bringToFront();
    // mymap.on('click', onMapClick);
    // mymap.on('click',function(e){
    // //     // getCursorXY;
    //     cX = event.clientX;
    //     cY = event.clientY;
    //     // alert(cX+"abc"+cY);
    //     getAPI();
    // })

    // function getAPI2(){
    //     axios.get('').then()
    // }
    function getAPI(){axios.get('http://10.103.227.77:8000/api/trash_images/9').then(function(response) {//http://10.103.227.77:8000/api/trash_images/3
        // console.log(response);
        // alert(JSON.stringify(response.data));
        // alert('response headers:\n\n' + JSON.stringify(response.headers));
        // console.log(response.toString())
        // var obj = JSON.parse('{"abc":[6,6]}');
        // alert('start');

        console.log(response.data);
        obj=response.data;
        // var obj = JSON.parse(response.data);
        // alert(JSON.parse(response));
        coorX=obj.location[0];
        coorY=obj.location[1];
        // alert(coorX);
        // alert(coorY);
        var mymap = L.map('mapid').setView([coorX,coorY
        ], 13);
        L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
            maxZoom: 18,
            attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
                '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
                'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
            id: 'mapbox.streets'
        }).addTo(mymap);
        L.marker([coorX,coorY]).addTo(mymap);
        // L.marker([51.5,0.09]).addTo(mymap);
        //     .bindPopup("<b>Hello world!</b><br />I am a popup.").openPopup();
        density=obj.trash_density;
        // b64=obj.image;
        // picture=picBase64.atob(b64);
        picUrl=null;
    }, function(err) { console.log(err) });
    };


</script>


<style type="text/css" scoped>
    #mapid { height: 600px; width:800px; }
    #Picture{
        height:300px;
        width:300px;
        position:absolute;
        /*background-color: blue;*/
        z-index: 999;
        top:20px;
        left:20px;
        border: 0px;
        display: none;
    }
</style>


