<!-- Author Hiroki Okubo -->
<template>
  <v-app>
    <v-main>
      <v-btn to="/postTimeline">
        <span>タイムラインを投稿</span>
      </v-btn>
      <v-container class="fill-height" fluid>
        <v-container v-if="is_friend">
          <v-row dense>
            <v-card>タイムライン</v-card>
            <v-spacer></v-spacer>
            <v-col v-for="(timeline) in timelines_list" :key="timeline.id" cols="12">
              <v-card v-bind:to="getIndividualURL(getFriendUserId(timeline.user_id))">
                <div class="d-flex flex-no-wrap justify-space-between">
                  <v-col>
                    <v-row style="margin : 0 auto;">
                      <v-avatar size="70" style="margin:1%;">
                        <img :src="avatar(timeline.user_id)" :alt="getFriendName(timeline.user_id)" />
                      </v-avatar>
                    </v-row>
                    <v-row style="margin : 0 auto;">
                      <span class="headline" style="text-align:right;">
                        {{
                        getFriendName(timeline.user_id)
                        }}
                      </span>
                    </v-row>
                  </v-col>
                  <v-col>
                    <div>
                      <v-card-title class="headline" v-text="timeline.statics"></v-card-title>
                      <v-card-subtitle
                        style="display: inline-block; text-align: center; font-size:120%;"
                      >{{ timeline.content }}</v-card-subtitle>
                      <v-card-subtitle>
                        <v-row>{{ processDate(timeline.event_date) }}</v-row>
                        <v-row>{{ timeline.place }}</v-row>
                      </v-card-subtitle>
                    </div>
                  </v-col>
                </div>
              </v-card>
            </v-col>
          </v-row>
        </v-container>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import moment from "moment";
export default {
  layout: "defaut",

  data: () => ({
    is_friend: false,
    friend_list: [],
    timelines_list: [],
  }),
  methods: {
    findData: async function () {
      let userid = this.$store.state.user.userInfo.id;
      const res = await this.$axios.$get("/timelines", {
        params: { user_id: userid },
      });
      const now = new Date().getTime();
      if (res != null) {
        this.timelines_list = res
          .sort(function (a, b) {
            return -(a.event_date - b.event_date);
          })
          .filter((n) => n.event_date > now);
      }
      const friends = await this.$axios.$get("/users/friends", {
        params: { id: userid },
      });

      if (friends != null) {
        this.is_friend = true;
        this.friend_list = friends;
      }
    },
    // Author Shotaro Murata
    processDate: function (date) {
      return moment(new Date(date)).format("YYYY/MM/DD HH:mm");
    },
    getFriendName: function (friend_id) {
      const matchFriends = this.friend_list.filter((n) => n.id == friend_id);
      if (!matchFriends.length) {
        return "";
      }
      return matchFriends[0].username;
    },
    getFriendUserId: function (friend_id) {
      console.log(friend_id);
      console.log(this.friend_list);
      const matchFriends = this.friend_list.filter((n) => n.id == friend_id);
      if (!matchFriends.length) {
        return "";
      }
      return matchFriends[0].user_id;
    },
    getIndividualURL(id) {
      return "/individual_user_info?user_id=" + id;
    },
  },
  created() {
    this.findData();
  },
  computed: {
    avatar() {
      return (id) => {
        const imageLen = 10;
        return `/user_icon_${(id % imageLen) + 1}.jpg`;
      };
    },
  },
};
</script>
