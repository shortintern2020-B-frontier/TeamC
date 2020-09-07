<!-- Author:ZHANG CHI-->
<template>
  <v-app>
    <v-app-bar app color="red" dense>
      <v-bottom-sheet v-model="staticSheet" persistent>
        <template v-slot:activator="{ on, attrs }">
          <v-btn depressed icon v-bind="attrs" v-on="on">
            <v-avatar color="" size="40">
              <img src="~/static/v.png" />
            </v-avatar>
          </v-btn>
        </template>
        <v-sheet class="text-center">
          <v-btn @click="sheet = !sheet">Save</v-btn>
          <v-divider vertical inset></v-divider>
          <v-btn @click="staticSheet = !staticSheet">close</v-btn>
          <div>
            Static
          </div>
        </v-sheet>
      </v-bottom-sheet>
      <v-menu
        v-model="comment"
        bottom
        right
        transition="scale-transition"
        origin="top left"
      >
        <template v-slot:activator="{ on }">
          <v-chip label pill v-on="on">
            {{UserName}}
          </v-chip>
        </template>
        <v-card width="300">
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title>Want Eatting</v-list-item-title>
              <v-list-item-subtitle>Mon, 12:30 PM</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-card>
      </v-menu>
    </v-app-bar>
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
      <v-btn value="test2">
        <span>Nearby</span>
        <v-icon>mdi-map-marker</v-icon>
      </v-btn>
    </v-bottom-navigation>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    activeBtn: "",
    staticSheet: false,
    comment: "",
    UserName:"Null"
  }),
  methods: {
    // change coler for active Button in navigation 
    findData: function() {
      this.UserName=this.$store.state.user.userInfo.username
      this.activeBtn = this.$route.name;
    }
  },
  created() {
    this.findData();
  }
};
</script>
