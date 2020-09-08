<!-- Author:ZHANG CHI-->
<template>
  <v-app>
    <v-app-bar app color="red" dense></v-app-bar>
    <nuxt />
    <v-bottom-navigation app :value="activeBtn" color="purple lighten-1">
      <v-btn value="home">
        <span>Home</span>
        <v-icon>mdi-history</v-icon>
      </v-btn>
      <v-btn value="Chat">
        <span>account</span>
        <v-icon>mdi-account</v-icon>
      </v-btn>
      <v-btn value="test">
        <span>Favorites</span>
        <v-icon>mdi-heart</v-icon>
      </v-btn>
      <v-btn value="mypage" to="/mypage">
        <span>MyPage</span>
        <v-icon>mdi-map-marker</v-icon>
      </v-btn>
    </v-bottom-navigation>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    activeBtn: ""
  }),
  methods: {
    findRoute: function() {
      this.activeBtn = this.$route.name;
    }
  },
  created() {
    this.findRoute();
  }
};
</script>
