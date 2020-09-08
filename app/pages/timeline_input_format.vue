<!-- author Hiroki Okubo -->

<template>
  <form>
    <v-text-field
      v-model="title"
      :error-messages="titleErrors"
      :counter="10"
      label="Title"
      required
      @input="$v.title.$touch()"
      @blur="$v.title.$touch()"
    ></v-text-field>
    <v-text-field
      v-model="place"
      :error-messages="placeErrors"
      :counter="10"
      label="Place"
      required
      @input="$v.title.$touch()"
      @blur="$v.title.$touch()"
    ></v-text-field>
    <v-text-field
      v-model="time"
      :error-messages="timeErrors"
      :counter="10"
      label="Time"
      required
      @input="$v.title.$touch()"
      @blur="$v.title.$touch()"
    ></v-text-field>
    <v-checkbox
      v-model="checkbox"
      :error-messages="checkboxErrors"
      label="Do you agree?"
      required
      @change="$v.checkbox.$touch()"
      @blur="$v.checkbox.$touch()"
    ></v-checkbox>

    <v-btn class="mr-4" @click="submit">submit</v-btn>
    <v-btn @click="clear">clear</v-btn>
  </form>
</template>

<!-- ページ遷移イメージ -->
<!--
<nuxt-link v-for="room in chat_rooms"
:to=`room/${room.id}`>
<li>{{ room.name}}</li>
</nuxt-link> -->

<script>
import Vue from "vue";
import Status from "~/components/Status";
Vue.component("Status", Status);
export default {
  name: "mypage",
  async asyncData({ $axios }) {
    const data = await $axios.$get("/users/find", {
      params: { user_id: "string" },
    });
    return data;
  },
  methods: {
    setUserId: function () {},
    createJson: function (key, value) {
      var json;
      return (json[key] = value);
    },
    postProfile: async function () {
      console.log(this.id);
      var json;
      await this.$axios.$post("/users/update", {
        user_id: this.user_id,
        username: this.username,
        email: this.email,
        password: this.password,
        status: 0,
        comment: this.comment,
      });
    },
  },
  mounted: function () {},
};
</script>
