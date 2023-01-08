const state = {
  token: null,
};

const getters = {};

const actions = {};

const mutations = {
  SET_USER_TOKEN: (state, token) => 
  (state.token = token),
  SET_USER_EMAIL: (state, email) => 
  (state.email = email)
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};