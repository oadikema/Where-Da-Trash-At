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
        .catch(error => console.error('getUserMedia() error:', error))
    },
    methods: {
      capture () {
          const mediaStreamTrack = this.mediaStream.getVideoTracks()[0]
          const imageCapture = new window.ImageCapture(mediaStreamTrack)
          return imageCapture.takePhoto().then(blob => {
            var reader = new FileReader();
            reader.readAsDataURL(blob); 
            reader.onloadend = function() {
                var base64data = reader.result;                
                console.log(base64data);
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