<template>
  <div>
     <v-layout
      text-center
      wrap
      class = "my-10 py-10"
    >

    <v-flex mb-4>
        <h1 class="display-2 font-weight-bold mb-3" >
          Where Da Trash At?
        </h1>
        <h3>
          Incentivizing people to report trash and clean their surroundings. It's the Pokémon Go for sustainability!
        </h3>
        <p class="subheading font-weight-regular">
          <br>Load the web app on your phone, take a photo of a spot of trash, and get points for reporting it. 
          <br> OR
          <br>Find a spot of trash near you on the Trash Map, pick up the trash, upload a photo of the clean spot, and get even more points for clearing it!
        </p>
        <router-link class="take-picture-button mdl-button mdl-js-button mdl-button--fab mdl-button--colored" to="/camera">
      <v-btn x-large color = "primary">Take a Picture of Trash</v-btn>
    </router-link>
        <br><br>
        <!-- <router-link class = "view-map" to= "http://127.0.0.1:5500/public/Sample.html"> -->

        <v-btn  href="http://127.0.0.1:5500/public/Sample.html"  x-large color = "primary">View Trash Map</v-btn>
        <!-- </router-link> -->
      </v-flex>

    
    
    



    </v-layout>

  </div>
</template>


  


<script>
export default {
  components: {
  
  },
};
</script>

<style scoped>

</style>