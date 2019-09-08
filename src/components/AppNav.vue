<template>
    <div>
        <!-- NAVIGATION DRAWER -->
        <v-navigation-drawer
        v-model="drawer"
        app
        >
        <v-list dense>
            <v-list-item @click="">
            <v-list-item-action>
                <v-icon>mdi-home</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <router-link class = "home-btn" to= "/">
                <v-list-item-title>Home</v-list-item-title>
                </router-link>
            </v-list-item-content>
            </v-list-item>
            <v-list-item @click="">
            <v-list-item-action>
                <v-icon>mdi-camera</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <router-link class = "camera-btn" to= "/camera">
                <v-list-item-title>Camera</v-list-item-title>
                </router-link>
            </v-list-item-content>
            </v-list-item>
            <v-list-item @click="">
            <v-list-item-action>
                <v-icon>mdi-map</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <router-link class = "map-btn" to= "/map">
                <v-list-item-title>Map</v-list-item-title>
                </router-link>
            </v-list-item-content>
            </v-list-item>
        </v-list>
        </v-navigation-drawer>

        <!-- NAVIGATION BAR -->
        <v-app-bar
      app
      color="indigo"
      dark
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <!-- <v-toolbar-title></v-toolbar-title> -->

        <!-- <v-toolbar-items>
          <v-btn text>Link 1</v-btn>
          <v-btn text>Link 3</v-btn>
        </v-toolbar-items> -->

    </v-app-bar>

    </div>
</template>

<script>
  export default {
    props: {
      source: String,
    },
    data: () => ({
      drawer: false,
    }),
  }
</script>

<style scoped>

</style>