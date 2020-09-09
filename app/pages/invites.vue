<!-- Author:TomuHirata-->
<template>
  <v-layout column justify-center align-center>
    <v-flex xs12 sm8 md6>
      <div class="text-center">
        <v-list three-line style="max-height: 500px" class="overflow-y-auto">
          <template v-for="invite in invites">
            <v-list-item true :key="invite.id">
              <template
                v-for="friend in invite.users"
              >
                <v-list-item-avatar
                  :key="`${invite.id}_${friend.id}`"
                >
                  <img
                    :src="avatar(friend.id)"
                    :alt="friend.username"
                  >
                </v-list-item-avatar>
                <span class="headline" :key="`name_${invite.id}_${friend.id}`">
                  {{ friend.username }}
                </span>
              </template>
              <v-list-item-content>
                <v-list-item-title>お誘いがあります</v-list-item-title>
                <v-list-item-subtitle>
                  <v-btn @click="handleClick(invite)">
                    <span>承認</span>
                    <!-- <v-icon>mdi-home</v-icon> -->
                  </v-btn>
                </v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </template>
        </v-list>
      </div>
    </v-flex>
  </v-layout>
</template>

<script>
import { mapState } from 'vuex';
export default {
    async created() {
    const res = await this.$axios.get("/invites/", {
      params: {
        user_id: this.$store.state.user.userInfo.id,
      },
    });
    this.invites = res.data;
  },

  data: () => ({
    invites: []
  }),
  computed: {
    ...mapState('user', ['userInfo']),
    avatar() {
      return (id) => {
        const imageLen = 10;
        return `/user_icon_${id % imageLen + 1}.jpg`;
      }
    }
  },
  methods: {
    async handleClick(invite) {
      const { id, chat_room_id } = invite;
      const user_id = this.userInfo.id;
      await this.$axios.post('invites/agree', {
        chat_room_id,
        user_id,
      });
      this.invites = this.invites.filter(n => n.id != id);
      alert('招待を承認しました');
    }
  }
};
</script>
