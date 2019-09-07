<template>
     <div id="mapid"></div>
</template>


<script>
import L from 'leaflet';


export default {
    name: 'Map',

    createMap(){
         mymap = L.map('mapid').setView([51.505, -0.09], 13);var mymap = L.map('mapid').setView([51.505, -0.09], 13);

        L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={pk.eyJ1IjoiYXJjdGljbWFyayIsImEiOiJjazA5cjBhZXgwNTN4M2hveDh0czU5MDI1In0.SemM2-S3Ejrnavic5kBijQ}', {
	attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
	maxZoom: 18,
	id: 'mapbox.streets',
	accessToken: 'your.mapbox.access.token'
}).addTo(mymap);
    }
    
}
</script>


<style scoped>
#mapid { height: 180px; } */
</style>