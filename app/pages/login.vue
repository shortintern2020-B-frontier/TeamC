// Author: ZHANG CHI
<template>
  <v-app>
    <v-main>
      <v-container
        class="fill-height"
        fluid
      >
        <v-row
          align="center"
          justify="center"
        >
          <v-col
            cols="12"
            sm="8"
            md="4"
            align="center"
            justify="center"
          >
            <v-avatar color="" size="62">
              <img
                src="~/static/v.png"
                alt="logo"
              >
            </v-avatar>
            <v-card-title 
              class="layout justify-center"
              disabled="true"
            >
              ゆる～くつながる
            </v-card-title>
            <v-spacer></v-spacer>
              <v-expand-transition>
                <v-card
                  v-show="expand"
                  class="mx-auto"
                >
                  <v-card-text>
                    <v-text-field
                      id="username"
                      label="Maill Address"
                      name="login"
                      prepend-icon="mdi-account"
                      type="text"
                    ></v-text-field>
                    </v-card-text>
                  <v-card-text>
                    <v-text-field
                      label="password"
                      name="password"
                      prepend-icon="mdi-lock"
                      type="password"
                    ></v-text-field>
                  </v-card-text>
                </v-card>
              </v-expand-transition>
            <v-card-actions
              class="layout justify-center"
            >
              <v-btn
                ref="register"
                large
                color="red"
                class="layout justify-center"
                nuxt
                to="/inspire"
              >
                新規作成
              </v-btn> 
            </v-card-actions>
            <v-divider></v-divider>
            <v-card-actions>
              <v-btn 
                small
                color="gray"
                class="layout justify-center"
                @click="expand = !expand"
                @click.prevent="del"
              >
                ログイン
              </v-btn>
            </v-card-actions>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
    
  </v-app>
</template>

<script>
  export default {
    layout: 'login',
    data: () => ({
    expand: false,
  }),
  methods: {
      del () {
        console.log(this.$refs.button.color);
      },
    },
  }
  

</script>
