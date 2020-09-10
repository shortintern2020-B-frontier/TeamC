<!-- Author:ZHANG CHI-->
<template>
  <v-app>
    <v-row justify="center">
      <v-app-bar app color="deep-purple" dense>
        <v-col cols="12" sm="8" md="6">
          <v-bottom-sheet v-model="statusShell" persistent>
            <template v-slot:activator="{ on, attrs }">
              <v-btn depressed icon v-bind="attrs" v-on="on">
                <v-avatar color="" size="40">
                  <img :src="avatar(userInfo.id)" />
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
                      color="deep-purple accent-3"
                      v-model="comment"
                      id="comment"
                      label="Comment(Optional)"
                      name="comment"
                      prepend-icon="mdi-message"
                      type="text"
                    ></v-text-field>
                  </v-form>
                  <v-card>
                    <p>{{ choosedStatusLabel || "null" }}</p>
                    <v-radio-group
                      v-model="choosedStatus"
                      :mandatory="false"
                      v-for="status in statusList"
                      :key="status.id"
                    >
                      <v-radio
                        color="deep-purple accent-3"
                        v-bind:label="status.title"
                        v-bind:value="status.id"
                        v-bind:class="status.class"
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
              <v-chip color="deep-purple lighten-5" label pill v-on="on">
                {{ originalStatus }}
                <v-icon right>
                  {{ statusList[status].class }}
                </v-icon>
              </v-chip>
            </template>
            <v-card width="300">
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title>
                    {{ originalcomment }}
                  </v-list-item-title>
                  <v-list-item-subtitle>
                    {{ commentTime }}
                  </v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-card>
          </v-menu>
          <v-divider class="mx-4" vertical></v-divider>
          <v-btn
            color="deep-purple darken-1"
            inset
            depressed
            to="/searchFriend"
            class="white--text"
          >
            Add Friends
          </v-btn>
        </v-col>
      </v-app-bar>
    </v-row>
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
        <span>Timeline</span>
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
import { mapState } from "vuex";
export default {
  data: () => ({
    activeBtn: "",
    statusShell: false,
    comment: "",
    status: 0,
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
        const user = await this.search();
        this.$store.commit("user/add", user);
      } else {
        this.updateflag = true;
      }
      this.user_id = this.$store.state.user.userInfo.user_id;
      this.status = this.$store.state.user.userInfo.status;
      this.choosedStatus = this.$store.state.user.userInfo.status;
      this.originalStatus = this.showStatusName(
        this.$store.state.user.userInfo.status
      );
      this.choosedStatusLabel = this.originalStatus;
      if (this.$store.state.user.userInfo.comment == "") {
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
        url: "/users/update",
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
          statusName = "Free";
          break;
        case "1":
        case 1:
          statusName = "Busy";
          break;
        case "2":
        case 2:
          statusName = "Movie";
          break;
        case "3":
        case 3:
          statusName = "Karaoke";
          break;
        case "4":
        case 4:
          statusName = "Food";
          break;
        case "5":
        case 5:
          statusName = "Sports";
          break;
        case "6":
        case 6:
          statusName = "Shopping";
          break;
        case "7":
        case 7:
          statusName = "Sleeping";
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
  },
  computed: {
    ...mapState("user", ["statusList", "userInfo"]),
    avatar() {
      return id => {
        const imageLen = 10;
        return `/user_icon_${(id % imageLen) + 1}.jpg`;
      };
    }
  }
};
</script>
