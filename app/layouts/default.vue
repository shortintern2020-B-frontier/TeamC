<!-- Author:ZHANG CHI-->
<template>
  <v-app>
    <v-app-bar app color="red"></v-app-bar>
    <v-main>
      <v-container>
        <nuxt />
      </v-container>
    </v-main>
    <v-bottom-navigation app :value="activeBtn" color="purple lighten-1">
      <v-btn>
        <span>Home</span>
        <v-icon>mdi-history</v-icon>
      </v-btn>
      <v-btn>
        <span>account</span>
        <v-icon>mdi-account</v-icon>
      </v-btn>
      <v-btn>
        <span>Favorites</span>
        <v-icon>mdi-heart</v-icon>
      </v-btn>
      <v-btn>
        <span>Nearby</span>
        <v-icon>mdi-map-marker</v-icon>
      </v-btn>
      <v-btn>
        <span>test</span>
        <v-icon>mdi-map-marker</v-icon>
      </v-btn>
    </v-bottom-navigation>
  </v-app>
</template>

<script>
</script>
