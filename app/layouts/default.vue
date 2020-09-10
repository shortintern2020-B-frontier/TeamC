<!-- Author:ZHANG CHI-->
<template>
  <v-app>
    <v-app-bar app color="deep-purple" dense></v-app-bar>
    <nuxt />
    <v-bottom-navigation app :value="activeBtn" color="deep-purple">
      <v-btn value="home" to="/home">
        <span>Home</span>
        <v-icon>mdi-home</v-icon>
      </v-btn>
      <v-btn value="chat-list" to="/chat-list">
        <span>Chat</span>
        <v-icon>mdi-chat</v-icon>
      </v-btn>
      <v-btn value="timeline" to="/timeline">
        <span>TimeLine</span>
        <v-icon>mdi-timeline</v-icon>
      </v-btn>
      <v-btn value="invites" to="/invites">
        <span>Invites</span>
        <v-icon>mdi-chat</v-icon>
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
  middleware: ["getPosition", "loginAuth"],
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
