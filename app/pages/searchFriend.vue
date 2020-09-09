<!-- Author:Shotaro Murata-->
<template>
  <v-app>
    <v-main>
      <div id="page">
        <div id="search">
          <v-toolbar dark color="teal">
            <v-autocomplete
              v-model="select"
              :search-input.sync="search_id"
              cache-items
              class="mx-4"
              flat
              hide-no-data
              hide-details
              label="ID"
              solo-inverted
            ></v-autocomplete>
            <v-btn @click="search">検索</v-btn>
          </v-toolbar>
        </div>

        <div id="user">
          <v-card class="mx-auto" v-if="target_username">
            <v-card-text>
              <v-row align="center">
                <v-col :key="1">
                  <img src="@/static/v.png" alt="icon" width="92" />
                </v-col>
                <v-col :key="2">
                  <v-row :key="1" style="font-weight: bold; font-size: 200%;">
                    <p>{{target_username}}</p>
                  </v-row>
                  <v-row :key="2" width="20">ひとこと: {{target_comment}}</v-row>
                </v-col>
              </v-row>
              <v-row align="center">
                <v-btn
                  style="display: inline-block; text-align: center; margin: 0 auto;"
                  @click="addFriend"
                  v-if="!isFriend"
                >追加</v-btn>
                <v-card
                  style="display: inline-block; text-align: center; margin: 0 auto;"
                  v-if="isFriend"
                >追加済</v-card>
              </v-row>
            </v-card-text>
          </v-card>
        </div>
      </div>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "searchFriend",
  components: {},
  data: () => ({
    target_username: "",
    isFriend: false,
  }),
  methods: {
    search: async function () {
      const res = await this.$axios.$get("/users/find", {
        params: { user_id: this.search_id },
      });
      const friends = await this.$axios.$get("/users/friends", {
        params: { id: this.$store.state.user.userInfo.id },
      });
      if (res != null) {
        this.target_username = res.username;
        this.target_comment = res.comment;
        this.target_id = res.id;
        if (
          friends.filter(
            (f) => f.user_id == res.id && f.username == res.username
          ).length != 0
        ) {
          this.isFriend = true;
        } else {
          this.isFriend = false;
        }
      } else {
        alert("error: user is not found!");
      }
    },
    addFriend: async function () {
      await this.$axios.$post("/users/friends", {
        user_id: this.$store.state.user.userInfo.id,
        target_user_id: this.target_id,
      });
      this.isFriend = true;
    },
  },
};
</script>