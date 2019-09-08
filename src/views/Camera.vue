<template>
  <div class="camera-modal">
    <video ref="video" class="camera-stream"/>
    <div><button id="snap" v-on:click="capture()">Snap Photo</button></div>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        mediaStream: null
      }
    },
    mounted () {
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
            console.log(blob)
  })
      }
    }
  }
</script>