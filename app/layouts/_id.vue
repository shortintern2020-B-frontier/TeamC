<!-- Author:ZHANG CHI-->
<template>
  <v-app>
    <v-app-bar app color="red" dense>
        <v-btn value="back" to="/chat-list">back</v-btn>
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
