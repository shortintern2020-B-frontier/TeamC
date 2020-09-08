<!-- author Hiroki Okubo & Shotaro Murata-->

<template>
  <v-app style="margin:5%;">
    <v-main>
      <form align="center">
        <h1 style="display: inline-block; text-align: center; margin: 0 auto;">タイムライン</h1>
        <v-text-field v-model="title" :counter="10" label="Title" required></v-text-field>
        <v-text-field v-model="place" :counter="10" label="Place" required></v-text-field>
        <v-text-field v-model="date" :counter="10" label="Time" required></v-text-field>
        <v-text-field v-model="comment" :counter="10" label="Comment" required></v-text-field>
        <!-- <v-checkbox
          v-model="checkbox"
          label="Do you agree?"
          required
          @change="$v.checkbox.$touch()"
          @blur="$v.checkbox.$touch()"
        ></v-checkbox>-->

        <v-btn class="mr-4" @click="submit">submit</v-btn>
        <v-btn @click="clear">clear</v-btn>
      </form>
    </v-main>
  </v-app>
</template>

<!-- ページ遷移イメージ -->
<!--
<nuxt-link v-for="room in chat_rooms"
:to=`room/${room.id}`>
<li>{{ room.name}}</li>
</nuxt-link> -->

<script>
export default {
  name: "mypage",
  data: () => ({
    title: "",
    place: "",
    date: "",
    comment: "",
  }),
  methods: {
    submit: async function () {
      await this.$axios.$post("/users/timeline", {
        user_id: this.$store.state.user.userInfo.id,
        place: this.place,
        date: this.date,
        comment: this.comment,
      });
    },
    clear: function () {
      this.title = "";
      this.place = "";
      this.data = "";
      this.comment = "";
    },
  },
};
</script>
