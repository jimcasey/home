# Slack Deep Link

Takes a Slack permalink and creates a deep link, optionally opening the link in Slack app or copying it to the clipboard. 

## Configuration

In order to use this workflow, it needs to be configured with your Slack team ID (`teamID`). See this article for how to locate your team ID:

	https://help.socialintents.com/article/148-how-to-find-your-slack-team-id-and-slack-channel-id

## Usage

- Open a permalink directly in Slack: `slack [permalink]`
- Copy a deeplink to the clipboard: `slink [permalink]`

For example, take the following permalink:

	https://my-team.slack.com/archives/C0346P4D3KQ/p1684323437504349

The following deep link will be created:

	slack://channel?team=T14Q6KC4N&id=C0346P4D3KQ&message=p1684323437504349

## Resources

- Deep linking in Slack's API documentation: https://api.slack.com/reference/deep-linking
- Copying links in Slack: https://slack.com/help/articles/203274767-Forward-messages-in-Slack#copy-a-link-to-a-message
