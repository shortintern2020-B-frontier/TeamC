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
          <v-btn @click="saveStatic">Save</v-btn>
          <v-divider vertical inset></v-divider>
          <v-btn @click="staticSheet = !staticSheet">close</v-btn>
          <div class="fill-height" fluid align="center" justify="center">
            <v-card width="300">
              <v-form>
                <v-text-field
                  v-model="comment"
                  id="comment"
                  label="Comment(Optional)"
                  name="comment"
                  prepend-icon="mdi-account"
                  type="text"
                ></v-text-field>
              </v-form>
              <v-card>
                <p>{{ choosedStaticLabel || "null" }}</p>
                <v-radio-group v-model="choosedStatic" :mandatory="false">
                  <v-radio
                    label="Busy"
                    value="0"
                    @click="showStaticLabel"
                  ></v-radio>
                  <v-radio
                    label="Free"
                    value="1"
                    @click="showStaticLabel"
                  ></v-radio>
                  <v-radio
                    label="Radio 3"
                    value="2"
                    @click="showStaticLabel"
                  ></v-radio>
                  <v-radio
                    label="Radio 4"
                    value="3"
                    @click="showStaticLabel"
                  ></v-radio>
                </v-radio-group>
              </v-card>
            </v-card>
          </div>
        </v-sheet>
      </v-bottom-sheet>
      <v-menu bottom right transition="scale-transition" origin="top left">
        <template v-slot:activator="{ on }">
          <v-chip label pill v-on="on">
            {{ originalStatic }}
          </v-chip>
        </template>
        <v-card width="300">
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title>{{ originalcomment }}</v-list-item-title>
              <v-list-item-subtitle>{{ commentTime }}</v-list-item-subtitle>
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
    originalStatic: "Static",
    originalcomment: "Your Comment",
    commentTime: "2020-09-08 09:00:00",
    choosedStatic: "0",
    choosedStaticLabel: "Busy"
  }),
  methods: {
    findData: function() {
      if (this.$store.state.user.userInfo.static != undefined) {
        this.originalStatic = this.$store.state.user.userInfo.static;
        if (this.$store.state.user.userInfo.comment == null) {
          this.originalcomment = this.originalStatic;
        } else {
          this.originalcomment = this.$store.state.user.userInfo.comment;
        }
        this.commentTime = this.$store.state.user.userInfo.status_update_at;
      } else {
      }
      this.activeBtn = this.$route.name;
    },
    saveStatic() {
      let _this = this;
      const { comment, choosedStatic } = this;
      if (condition) {
      }
      // this.$axios({
      //   method: "post",
      //   url: "http://127.0.0.1:8000/",
      //   data: { comment: comment, static: choosedStatic }
      // })
      //   .then(function(response) {
      //     if (response.data == null) {
      //     } else {
      //       _this.staticSheet = !this.staticSheet;
      //       _this.findData();
      //     }
      //   })
      //   .catch(function(error) {
      //     console.log(error);
      //   });
    },
    showStaticLabel() {
      switch (this.choosedStatic) {
        case "0":
          this.choosedStaticLabel = "Busy";
          break;
        case "1":
          this.choosedStaticLabel = "Free";
          break;
        case "2":
          this.choosedStaticLabel = "test2";
          break;
        case "3":
          this.choosedStaticLabel = "test3";
          break;
        default:
          this.choosedStaticLabel = "Busy";
          break;
      }
    }
  },
  created() {
    this.findData();
  }
};
</script>
