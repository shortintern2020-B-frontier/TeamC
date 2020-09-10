<!-- Author:Shotaro Murata-->
<template>
  <v-app>
    <v-main style="margin:5%;">
      <form>
        <div id="profile">
          <div id="icon">
            <v-avatar>
              <img :src="avatar(user.id)" />
            </v-avatar>
          </div>
          <v-text-field v-model="user.user_id" :counter="10" label="ID" required></v-text-field>
          <v-text-field v-model="user.username" label="Name" required></v-text-field>
          <v-text-field v-model="user.email" label="E-mail" required></v-text-field>
        </div>
        <div id="status">
          <h2>Status</h2>
          <v-text-field v-model="user.comment" label="Comment"></v-text-field>
          <ul id="example-1">
            <div v-for="item in statusList" :key="item.id" style="padding: 10px;">
              <input type="radio" v-bind:id="item.id" v-bind:value="item.id" v-model="user.status" />
              <i v-bind:class="item.class" />
              <label>{{item.title}}</label>
            </div>
          </ul>
        </div>
        <v-btn @click="postProfile">プロフィールを更新する</v-btn>
      </form>
    </v-main>
  </v-app>
</template>

<script>
import { mapState } from "vuex";
export default {
  data() {
    return {
      user: {},
    };
  },
  async asyncData({ store }) {
    return {
      user: { ...store.state.user.userInfo },
    };
  },
  methods: {
    store: function(data) { 
      this.$store.commit("user/add", data)
    },
    postProfile: async function () {
      const res = await this.$axios.$post("/users/update", {
        id: this.user.id,
        user_id: this.user.user_id,
        username: this.user.username,
        email: this.user.email,
        status: this.user.status,
        comment: this.user.comment,
      }).then((data) => {
        if (data != null) {
          this.user.status_update_at = data.status_update_at
          this.$store.commit("user/add", this.user)
        }
      })
      .catch(function(error) {
        console.log(error);
      });
      
    }
  },
  computed: {
    ...mapState("user", ["statusList", "userInfo"]),
    avatar() {
      return (id) => {
        const imageLen = 10;
        return `/user_icon_${id % imageLen + 1}.jpg`;
      }
    }
  },
};
</script>

