def approve(client, assignmentId):
    client.approve_assignment(
        AssignmentId=assignmentId,
        RequesterFeedback='Good job man!',
        OverrideRejection=False
    )


def reject(client, assignmentId):
    client.reject_assignment(
        AssignmentId=assignmentId,
        RequesterFeedback='Damn man, you aswered randomly!'
    )
