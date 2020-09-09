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
              <v-card>
                <div class="d-flex flex-no-wrap justify-space-between">
                  <v-avatar size="100" tile>
                    <span class="white--text headline">
                      {{
                      getFriendName(timeline.user_id)
                      }}
                    </span>
                  </v-avatar>
                  <div>
                    <v-card-title class="headline" v-text="timeline.statics"></v-card-title>
                    <v-card-subtitle>{{ timeline.content }} + {{ processDate(timeline.event_date) }} + {{ timeline.place }}</v-card-subtitle>
                  </div>
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
export default {
  layout: "home",
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
      if (res != null) {
        this.timelines_list = res;
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
      return new Date(date);
    },
    getFriendName: function (friend_id) {
      return this.friend_list.filter((n) => n.id == friend_id)[0].username;
    },
  },
  created() {
    this.findData();
  },
};
</script>
