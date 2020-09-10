<!-- Author Hiroki Okubo -->
<template>
  <v-app>
    <v-main>
      <div class="text-center">
      <v-btn to="/postTimeline">
        <span>Post timeline</span>
      </v-btn>
      </div>
      <v-container class="fill-height" fluid >
        <v-container v-if="is_friend">
          <v-row dense>
            <v-card>No Timeline</v-card>
            <v-spacer></v-spacer>
            <v-col v-for="(timeline) in timelines_list" :key="timeline.id" cols="12">
              <v-card>
                <div class="d-flex flex-no-wrap justify-space-between">
                    <v-avatar size="70">
                      <img :src="avatar(getFriendId(timeline.user_id))" :alt="getFriendName(timeline.user_id)" />
                    </v-avatar>
                    <span class="headline">
                      {{
                      getFriendName(timeline.user_id)
                      }}
                    </span>
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
      const matchFriends = this.friend_list.filter((n) => n.id == friend_id);
      if(!matchFriends.length){
        return '';
      }
      return matchFriends[0].username;
    },
    getFriendId: function (friend_id) {
      const matchFriends = this.friend_list.filter((n) => n.id == friend_id);
      if(!matchFriends.length){
        return '';
      }
      return matchFriends[0].id;
    },
  },
  created() {
    this.findData();
    
  },
  computed: {
    avatar() {
      return id => {
        const imageLen = 10;
        return `/user_icon_${(id % imageLen) + 1}.jpg`;
      };
    }
  },
};
</script>
