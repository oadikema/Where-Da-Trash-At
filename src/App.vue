<template>
  <v-app>
  <AppNav />

    <v-content>
       <v-container fluid>
         <router-view>
            <!-- <HelloWorld/> -->
            <!-- All specific views will be determined by the view router -->
         </router-view>
       </v-container>
    </v-content>

    <v-footer
      color="indigo"
      app
    >
      <span class="white--text">&copy; Trash Trackers 2019</span>
    </v-footer>
  </v-app>
</template>

<script>
import AppNav from  './components/AppNav'

export default {
  name: 'App',
  components: {
   
    AppNav,
  },
  data: () => ({
    //
  }),
};
</script>

