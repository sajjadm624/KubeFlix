{{- define "auth-service.name" -}}
auth-service
{{- end }}

{{- define "auth-service.fullname" -}}
{{ .Release.Name }}-auth-svc
{{- end }}
