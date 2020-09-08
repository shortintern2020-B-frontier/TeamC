<!-- Author:ZHANG CHI-->
<template>
  <v-app>
    <v-row justify="center">
      <v-app-bar app color="red" dense>
        <v-col cols="12" sm="8" md="6">
          <v-bottom-sheet v-model="statusShell" persistent>
            <template v-slot:activator="{ on, attrs }">
              <v-btn depressed icon v-bind="attrs" v-on="on">
                <v-avatar color="" size="40">
                  <img src="~/static/v.png" />
                </v-avatar>
              </v-btn>
            </template>
            <v-sheet class="text-center">
              <v-btn @click="saveStatus">Save</v-btn>
              <v-divider vertical inset></v-divider>
              <v-btn @click="statusShell = !statusShell">close</v-btn>
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
                    <p>{{ choosedStatusLabel || "null" }}</p>
                    <v-radio-group v-model="choosedStatus" :mandatory="false">
                      <v-radio
                        label="Busy"
                        value="0"
                        @click="showStatusLabel"
                      ></v-radio>
                      <v-radio
                        label="Free"
                        value="1"
                        @click="showStatusLabel"
                      ></v-radio>
                      <v-radio
                        label="Radio 3"
                        value="2"
                        @click="showStatusLabel"
                      ></v-radio>
                      <v-radio
                        label="Radio 4"
                        value="3"
                        @click="showStatusLabel"
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
                {{ originalStatus }}
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
          <v-divider class="mx-13" vertical></v-divider>
          <v-btn color="red" inset to="/searchFriend">
            友達追加
          </v-btn>
        </v-col>
      </v-app-bar>
    </v-row>
    <nuxt />
    <v-bottom-navigation app :value="activeBtn" color="purple lighten-1">
      <v-btn value="home" to="/home">
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
    activeBtn: "",
    statusShell: false,
    comment: "",
    originalStatus: "status",
    originalcomment: "Your Comment",
    commentTime: "2020-09-08 09:00:00",
    choosedStatus: "0",
    choosedStatusLabel: "Busy",
    updateflag: false,
    user_id: ""
  }),
  methods: {
    search: async function() {
      const res = await this.$axios.$get("/users/find", {
        params: { user_id: this.user_id }
      });
      return res;
    },
    findData: async function() {
      if (this.updateflag) {
        const res = await this.search();
        this.$store.commit("user/add", res);
      } else {
        this.updateflag = true;
      }
      this.user_id = this.$store.state.user.userInfo.user_id;
      this.originalStatus = this.showStatusName(
        this.$store.state.user.userInfo.status
      );
      if (this.$store.state.user.userInfo.comment == null) {
        this.originalcomment = this.originalStatus;
      } else {
        this.originalcomment = this.$store.state.user.userInfo.comment;
      }
      this.commentTime = this.$store.state.user.userInfo.status_update_at;
      this.activeBtn = this.$route.name;
    },
    saveStatus() {
      let _this = this;
      const { comment, choosedStatus } = this;
      this.$axios({
        method: "post",
        url: "http://127.0.0.1:8000/users/update",
        data: {
          id: this.$store.state.user.userInfo.id,
          status: choosedStatus,
          comment: comment
        }
      })
        .then(function(response) {
          if (response.data == null) {
          } else {
            _this.statusShell = !_this.statusShell;
            _this.findData();
          }
        })
        .catch(function(error) {
          console.log(error);
        });
    },
    showStatusName(status) {
      let statusName = "";
      switch (status) {
        case "0":
        case 0:
          statusName = "Busy";
          break;
        case "1":
        case 1:
          statusName = "Free";
          break;
        case "2":
        case 2:
          statusName = "test2";
          break;
        case "3":
        case 3:
          statusName = "test3";
          break;
        default:
          statusName = "Busy";
          break;
      }
      return statusName;
    },
    showStatusLabel() {
      this.choosedStatusLabel = this.showStatusName(this.choosedStatus);
    }
  },
  created() {
    this.findData();
  }
};
</script>
