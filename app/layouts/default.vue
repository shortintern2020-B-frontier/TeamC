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
      <v-btn value="chat" to="/chat-list">
        <span>Chat</span>
        <v-icon>mdi-chat</v-icon>
      </v-btn>
      <v-btn value="timeline" to="/timeline">
        <span>TimeLine</span>
        <v-icon>mdi-map-timeline</v-icon>
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
<<<<<<< HEAD
  middleware: "getPosition",
=======
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
>>>>>>> a49c6a0d77e93603f1852efb313e8edd81492b11
};
</script>
