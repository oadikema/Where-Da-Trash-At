<template>
<v-layout
      text-center
      wrap
      class = "my-10 py-10"
    >

<v-flex mb-4>
  <div class="camera-modal">
    <h2> Do you see some trash? Take a photo of it! </h2>
    <video ref="video" class="camera-stream" width="640" height="480" />
    <div><v-btn x-large color = "primary" id="snap" v-on:click= "capture()">Snap Photo</v-btn></div>
    <h3 id= "geo"> Latitude: {{x.latitude}} <br>
    Longitude: {{x.longitude}}</h3>
  </div>
</v-flex>
  </v-layout>

</template>

<script>
import axios from "axios"


  export default {
    data () {
      return {
        mediaStream: null,
        x:{ latitude: null, 
            longitude: null
        }
        
      }
    },
    mounted () {
        this.getLocation()
        navigator.mediaDevices.getUserMedia({ video: true })
        .then(mediaStream => {
          this.mediaStream = mediaStream
          this.$refs.video.srcObject = mediaStream
          this.$refs.video.play()
        })
        //eslint-disable-next-line
        .catch(error => console.error('getUserMedia() error:', error))
    },
    methods: {
      capture () {
        var latitude = this.x.latitude;
        var longitude = this.x.longitude;
          const mediaStreamTrack = this.mediaStream.getVideoTracks()[0]
          const imageCapture = new window.ImageCapture(mediaStreamTrack)
          return imageCapture.takePhoto().then(blob => {
            var reader = new FileReader();
            reader.readAsDataURL(blob); 
            reader.onloadend = function() {
                var base64data = reader.result;
                var index = base64data.indexOf(',') + 1;


                base64data = base64data.slice(index)
                
                while(base64data.length %4 != 0)
                {
                  base64data += "=";
                }
                

                // console.log(base64data);

                

                let jsonObject = {

                  image: base64data,
                  coordinates: [latitude, longitude]
                }

              

                //eslint-disable-next-line
                let network_url = "http://10.103.227.77:8000/api/trash_images_post";
                //eslint-disable-next-line
                let local_url = 'http://localhost:8000/api/trash_images_post'

                axios.post(network_url, jsonObject)
                .then(response =>{
                  // eslint-disable-next-line
                  console.log(response);
                })
                .catch(error => {
                  // eslint-disable-next-line
                  console.log(error);
                })


                }
            })
      },
      getLocation() {
          navigator.geolocation.getCurrentPosition(this.showPosition);  
      },
      showPosition(position) {
        this.x.latitude = position.coords.latitude;
        this.x.longitude = position.coords.longitude;
        }
    }
}
</script>