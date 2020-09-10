<!-- Author:Shun Kiyoura-->
<template>
  <v-app>
    <v-app-bar color="deep-purple" app dense>
      <v-btn
        color="deep-purple darken-4"
        class="white--text"
        value="back"
        to="/chat-list"
        depressed
        >back</v-btn
      >
    </v-app-bar>
    <nuxt />
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
