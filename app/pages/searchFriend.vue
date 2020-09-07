<template>
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

    <div id="user" v-if="username">
      <v-card class="mx-auto">
        <v-card-text>
          <v-row align="center">
            <v-col :key="1">
              <img src="@/static/v.png" alt="icon" width="92" />
            </v-col>
            <v-col :key="2">
              <v-row :key="1" width="100" v-text="bold">{{username}}</v-row>
              <v-row :key="2" width="20">ひとこと: {{comment}}</v-row>
            </v-col>
          </v-row>
          <v-row align="center">
            <v-btn @click="addFriend">追加</v-btn>
          </v-row>
        </v-card-text>
      </v-card>
    </div>
  </div>
</template>

<script>
import Vue from "vue";
export default {
  name: "mypage",
  components: {},
  data: () => ({
    username: "",
  }),
  methods: {
    search: async function () {
      const res = await this.$axios.$get("/users/find", {
        params: { user_id: this.search_id },
      });
      this.username = res.username;
      this.comment = res.comment;
    },
    addFriend: async function () {
      // Todo
    },
  },
  computed: {},
  mounted: function () {},
};
</script>