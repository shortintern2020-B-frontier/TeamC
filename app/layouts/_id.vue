<!-- Author:Shun Kiyoura-->
<template>
  <v-app>
    <v-app-bar app dense>
      <v-btn text value="back" to="/chat-list">back</v-btn>
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
