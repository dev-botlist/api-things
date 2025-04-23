const { SlashCommandBuilder } = require('discord.js');
const axios = require('axios');

module.exports = {
  data: new SlashCommandBuilder()
    .setName('send-count')
    .setDescription('Sends the server count to the API'),

  async execute(interaction) {
    const serverCount = interaction.client.guilds.cache.size;
    const botID = "<YOUR_BOT_ID>";
    const token = '<YOUR_API_TOKEN>';
    // Replace with your bot ID and token

    await interaction.deferReply({ ephemeral: true });

    try {
      const res = await axios.post(`https://dev-botlist.com/api/${botID}/servercount`, {
        token,
        serverCount
      });

      await interaction.editReply({
        content: `✅ Server count successfully updated: **${serverCount}**`
      });
    } catch (err) {
      console.error(err);
      await interaction.editReply({
        content: `❌ Error while sending: ${err.response?.data?.message || err.message}`
      });
    }
  }
};
