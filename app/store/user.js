// Author: ZHANG CHI
export const state = () => ({
  userInfo: {}
})

export const mutations = {
  add(state, object) {
    state.userInfo = object;
  }
}

export const actions = {
}