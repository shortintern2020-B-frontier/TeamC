<!-- Author:ZHANG CHI-->
<template>
  <v-app>
    <v-app-bar app color="red" dense></v-app-bar>
    <nuxt />
    <v-bottom-navigation app :value="activeBtn" color="purple lighten-1">
      <v-btn value="home" to="/home">
        <span>Home</span>
        <v-icon>mdi-home</v-icon>
      </v-btn>
      <v-btn value="chat">
        <span>Chat</span>
        <v-icon>mdi-chat</v-icon>
      </v-btn>
      <v-btn value="timeline">
        <span>Timeline</span>
        <v-icon>mdi-timeline</v-icon>
      <v-btn to="/timeline">
        <span>TimeLine</span>
        <v-icon>mdi-map-marker</v-icon>
      </v-btn>
      <v-btn value="mypage" to="/mypage">
        <span>MyPage</span>
        <v-icon>mdi-account</v-icon>
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
